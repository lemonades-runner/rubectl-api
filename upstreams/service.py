from uuid import UUID, uuid4

from upstreams.repository import UpstreamsRepository
from upstreams.schemas import UpstreamCreate
from utils.unitofwork import IUnitOfWork


class UpstreamsService:
    def __init__(self, repository: UpstreamsRepository):
        self.repository = repository

    async def read_upstreams(self, uow: IUnitOfWork, deployment_uuid: UUID | None = None):
        async with uow:
            filter_by_dict = dict()
            if deployment_uuid:
                filter_by_dict['deployment_uuid'] = deployment_uuid
            upstreams = await self.repository.find_all(uow.session, **filter_by_dict)
            return upstreams

    async def read_upstream(self, uow: IUnitOfWork, uuid: UUID):
        async with uow:
            upstream = await self.repository.find_one(uow.session, uuid=uuid)
            return upstream

    async def create_upstream(self, uow: IUnitOfWork, upstream: UpstreamCreate):
        async with uow:
            uuid = uuid4()
            url = upstream.url.strip()
            deployment_uuid = upstream.deployment_uuid

            await self.repository.add_one(uow.session, {
                'uuid': uuid,
                'deployment_uuid': deployment_uuid,
                'url': url
            })

            # TODO notify load balancer

            await uow.commit()
            return uuid

    async def delete_upstream(self, uow: IUnitOfWork, uuid: UUID):
        async with uow:
            await self.repository.delete_one(uow.session, uuid=uuid)

            # TODO notify load balancer

            await uow.commit()
