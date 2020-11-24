from fastapi import APIRouter

from fastapi import Depends
from fastapi.security.api_key import APIKey

from api_key import get_api_key

from model.result_models import *

from controller.simple_example import SimpleExample



router = APIRouter()


@router.get("/{input}", response_model=SimpleExampleResults, tags=["SimpleExample"])
def get_result(
    input: int,
    apikey: APIKey = Depends(get_api_key)
):
    """Multipliziert den Input mit dem Faktor 5.
    ```
    /{input}&access_token={access_token}
    ```
    """
    controller = SimpleExample()

    return SimpleExampleResults(Response=controller.get_result(input))
