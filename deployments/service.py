from uuid import UUID, uuid4

from deployments.repository import DeploymentsRepository
from deployments.schemas import DeploymentCreate
from utils.unitofwork import IUnitOfWork


class DeploymentsService:
    def __init__(self, repository: DeploymentsRepository):
        self.repository = repository

    async def read_deployments(self, uow: IUnitOfWork):
        async with uow:
            deployments = await self.repository.find_all(uow.session)
            return deployments

    async def read_deployment(self, uow: IUnitOfWork, uuid: UUID):
        async with uow:
            deployment = await self.repository.find_one(uow.session, uuid=uuid)
            return deployment

    async def create_deployment(self, uow: IUnitOfWork, deployment: DeploymentCreate):
        async with uow:
            uuid = uuid4()
            name = deployment.name.strip()
            if not name:
                name = f'unique-deployment-name-{uuid}'
            image = deployment.image.strip()

            await self.repository.add_one(uow.session, {
                'uuid': uuid,
                'url': None,
                'name': name,
                'image': image
            })
            await uow.commit()
            return uuid

    async def delete_deployment(self, uow: IUnitOfWork, uuid: UUID):
        async with uow:
            await self.repository.delete_one(uow.session, uuid=uuid)
            await uow.commit()
