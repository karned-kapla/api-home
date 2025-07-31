import re
from typing import List
from urllib.parse import urlparse
from uuid import uuid4

from pymongo import MongoClient

from interfaces.home_interface import HomeRepository
from models.home_model import HomeWrite
from schemas.home_schema import list_home_serial, home_serial

def check_uri(uri):
    if not re.match(r"^mongodb://", uri):
        raise ValueError("Invalid URI: URI must start with 'mongodb://'")


def extract_database(uri: str) -> str:
    parsed_uri = urlparse(uri)
    db_name = parsed_uri.path.lstrip("/")

    if not db_name:
        raise ValueError("L'URI MongoDB ne contient pas de nom de base de données.")

    return db_name


class HomeRepositoryMongo(HomeRepository):

    def __init__(self, uri):
        check_uri(uri)
        database = extract_database(uri)

        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client[database]
        self.collection = "homes"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def create_home(self, home_create: HomeWrite) -> str:
        home_data = home_create.model_dump()
        home_id = str(uuid4())
        home_data["_id"] = home_id
        try:
            new_uuid = self.db[self.collection].insert_one(home_data)
            return new_uuid.inserted_id
        except Exception as e:
            raise ValueError(f"Failed to create home in database: {str(e)}")

    def get_home(self, uuid: str) -> dict:
        result = self.db[self.collection].find_one({"_id": uuid})
        if result is None:
            return None
        home = home_serial(result)
        return home

    def list_homes(self) -> List[dict]:
        result = self.db[self.collection].find()
        homes = list_home_serial(result)
        return homes

    def update_home(self, uuid: str, home_update: HomeWrite) -> None:
        update_fields = home_update.model_dump()
        update_fields.pop('created_by', None)
        update_data = {"$set": update_fields}
        self.db[self.collection].find_one_and_update({"_id": uuid}, update_data)


    def delete_home(self, uuid: str) -> None:
        self.db[self.collection].delete_one({"_id": uuid})

    def close(self):
        self.client.close()
