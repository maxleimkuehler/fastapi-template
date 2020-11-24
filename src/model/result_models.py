from pydantic import BaseModel


class HealthResult(BaseModel):
    Status: bool

class SimpleExampleResults(BaseModel):
    Response: int
