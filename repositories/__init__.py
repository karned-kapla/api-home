from typing import Type

from common_api.services.v0 import Logger
from repositories.home_repository_mongo import HomeRepositoryMongo

logger = Logger()


class Repositories:
    def __init__(self, home_repo=None):
        self.home_repo = home_repo


class BucketRepositories:
    def __init__(self, home_bucket_repo=None):
        self.home_bucket_repo = home_bucket_repo


def get_repositories(uri: str) -> Repositories | Type[Repositories]:
    if uri.startswith("mongodb"):
        logger.info("Using MongoDB repositories")
        return Repositories(
            home_repo = HomeRepositoryMongo(uri)
        )

    return Repositories


def get_bucket_repositories(credentials) -> BucketRepositories | Type[BucketRepositories]:

    return BucketRepositories
