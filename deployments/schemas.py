from uuid import UUID

from pydantic import BaseModel


class DeploymentRead(BaseModel):
    uuid: UUID
    url: str | None = None
    name: str
    image: str


class DeploymentCreate(BaseModel):
    name: str = ''
    image: str
