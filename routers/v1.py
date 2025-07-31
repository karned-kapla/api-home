from fastapi import APIRouter, HTTPException, status, Request
from config.config import API_TAG_NAME
from common_api.decorators.v0.check_permission import check_permissions
from models.home_model import HomeCreate, HomeRead, HomeUpdate
from common_api.services.v0 import Logger
from services.homes_service import create_home, get_homes, get_home, update_home, delete_home

logger = Logger()

VERSION = "v1"
api_group_name = f"/{API_TAG_NAME}/{VERSION}/"

router = APIRouter(
    tags=[api_group_name],
    prefix=f"/home/{VERSION}"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
@check_permissions(['create'])
async def create_new_home(request: Request, home: HomeCreate) -> dict:
    logger.api("POST /home/v1/")
    home.created_by = request.state.token_info.get('user_uuid')
    new_uuid = create_home(request, home)
    return {"uuid": new_uuid}


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[HomeRead])
@check_permissions(['read', 'read_own'])
async def read_homes(request: Request):
    logger.api("GET /home/v1/")
    return get_homes(request)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=HomeRead)
@check_permissions(['list', 'list_own'])
async def read_home(request: Request, uuid: str):
    logger.api("GET /home/v1/{uuid}")
    home = get_home(request, uuid)
    if home is None:
        raise HTTPException(status_code=404, detail="Home not found")
    return home


@router.put("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions(['update', 'update_own'])
async def update_existing_home(request: Request, uuid: str, home_update: HomeUpdate):
    logger.api("PUT /home/v1/{uuid}")
    update_home(request, uuid, home_update)


@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions(['delete', 'delete_own'])
async def delete_existing_home(request: Request, uuid: str):
    logger.api("DELETE /home/v1/{uuid}")
    delete_home(request, uuid)
