from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN

from services.credential_service import CredentialService

API_KEY_NAME = "access_token"

API_KEY_QUERY = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

async def get_api_key(
    api_key_query: str = Security(API_KEY_QUERY),
):
    credential_service = CredentialService()

    if credential_service.apikey_exists(api_key_query):
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
