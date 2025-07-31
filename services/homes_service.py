from fastapi import HTTPException
from models.home_model import HomeCreate, HomeUpdate
from common_api.utils.v0 import get_state_repos


def create_home(request, new_home) -> str:
    try:
        repos = get_state_repos(request)
        new_uuid = repos.home_repo.create_home(new_home)
        if not isinstance(new_uuid, str):
            raise TypeError("The method create_home did not return a str.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the home: {e}")

    return new_uuid

def get_homes(request) -> list[HomeCreate]:
    try:
        repos = get_state_repos(request)
        homes = repos.home_repo.list_homes()
        if not isinstance(homes, list):
            raise TypeError("The method list_homes did not return a list.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while get the list of homes: {e}")

    return homes


def get_home(request, uuid: str) -> HomeCreate:
    try:
        repos = get_state_repos(request)
        home = repos.home_repo.get_home(uuid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving the home: {e}")

    if home is None:
        raise HTTPException(status_code=404, detail="Home not found")

    return home

def update_home(request, uuid: str, home_update: HomeUpdate) -> None:
    try:
        repos = get_state_repos(request)
        repos.home_repo.update_home(uuid, home_update)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the home: {e}")

def delete_home(request, uuid: str) -> None:
    try:
        repos = get_state_repos(request)
        repos.home_repo.delete_home(uuid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the home: {e}")