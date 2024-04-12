from uuid import uuid4
from sqlalchemy import (Column, String, Uuid)
from utils.database import Base

from deployments.schemas import DeploymentRead


class Deployment(Base):
    __tablename__ = 'deployment'

    uuid = Column(Uuid, primary_key=True, default=uuid4)
    url = Column(String, nullable=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)

    def to_read_model(self) -> DeploymentRead:
        return DeploymentRead(
            uuid=self.uuid,
            url=self.url,
            name=self.name,
            image=self.image
        )
