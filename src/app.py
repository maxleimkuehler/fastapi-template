import logging

from fastapi import FastAPI
from routers import health, simple_example



log = logging.getLogger(__name__)

tags_metadata = [
    {
        "name": "Health",
        "description": "This API endpoint describes the status of the service.",
    },

    {
        "name": "SimpleExample",
        "description": "Simple Example.",
    }
]

description = "## General Information \n This is an API Template."


app = FastAPI(
    openapi_tags=tags_metadata,
    # https://fastapi.tiangolo.com/tutorial/metadata/#openapi-url
    title="Fast API Template",
    description=description,
    version="1.0",)


app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    simple_example.router,
    prefix="/example",
    tags=["SimpleExample"],
    responses={404: {"description": "Not found"}},
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
