from abc import ABC, abstractmethod
from typing import List
from models.home_model import HomeWrite

class HomeRepository(ABC):

    @abstractmethod
    def create_home(self, home_create: HomeWrite):
        pass

    @abstractmethod
    def get_home(self, home_id: str):
        pass

    @abstractmethod
    def list_homes(self):
        pass

    @abstractmethod
    def update_home(self, home_id: str, home_update: HomeWrite):
        pass

    @abstractmethod
    def delete_home(self, home_id: str):
        pass

    @abstractmethod
    def close(self):
        pass