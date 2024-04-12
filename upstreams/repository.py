from upstreams.models import Upstream
from utils.repository import SQLAlchemyRepository


class UpstreamsRepository(SQLAlchemyRepository):
    model = Upstream
