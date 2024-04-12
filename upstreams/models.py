from uuid import uuid4
from sqlalchemy import (Column, String, Uuid, ForeignKey)

from deployments.models import Deployment
from upstreams.schemas import UpstreamRead
from utils.database import Base


class Upstream(Base):
    __tablename__ = 'upstream'

    uuid = Column(Uuid, primary_key=True, default=uuid4)
    deployment_uuid = Column(Uuid, ForeignKey(Deployment.uuid), nullable=False)
    url = Column(String, nullable=False)

    def to_read_model(self) -> UpstreamRead:
        return UpstreamRead(
            uuid=self.uuid,
            deployment_uuid=self.deployment_uuid,
            url=self.url
        )
