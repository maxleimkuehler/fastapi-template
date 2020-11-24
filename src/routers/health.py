from fastapi import APIRouter

from controller.health_controller import HealthController
from model.result_models import HealthResult

router = APIRouter()


@router.get("", response_model=HealthResult, tags=["Health"])
async def get_health():
    """Returns the health status of the API
    A status `true` is good.
    If not, please  reach out to [max.leimkuehler@dfki.de](mailto:max.leimkuehler@dfki.de).

    ```json
    {
        "Status": true
    }
    ```
    """
    controller = HealthController()
    status = controller.check()
    return HealthResult(Status=status.status)
