from typing import Annotated

from fastapi import Depends, Header

from deployments.repository import DeploymentsRepository
from deployments.service import DeploymentsService

from upstreams.repository import UpstreamsRepository
from upstreams.service import UpstreamsService

from utils.unitofwork import IUnitOfWork, UnitOfWork

upstreams_repository = UpstreamsRepository()
upstreams_service = UpstreamsService(upstreams_repository)

deployments_repository = DeploymentsRepository()
deployments_service = DeploymentsService(deployments_repository)


async def get_deployments_service():
    return deployments_service


async def get_upstreams_service():
    return upstreams_service


DeploymentsServiceDep = Annotated[DeploymentsService, Depends(get_deployments_service)]
UpstreamsServiceDep = Annotated[UpstreamsService, Depends(get_upstreams_service)]

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
AuthenticationDep = Annotated[str | None, Header()]
