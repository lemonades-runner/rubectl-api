from deployments.models import Deployment
from utils.repository import SQLAlchemyRepository


class DeploymentsRepository(SQLAlchemyRepository):
    model = Deployment
