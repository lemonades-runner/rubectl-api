from uuid import UUID

from pydantic import BaseModel


class UpstreamRead(BaseModel):
    uuid: UUID
    deployment_uuid: UUID
    url: str


class UpstreamCreate(BaseModel):
    deployment_uuid: UUID
    url: str
