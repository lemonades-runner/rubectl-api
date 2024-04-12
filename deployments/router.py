from uuid import UUID

from fastapi import APIRouter

from deployments.exceptions import DeploymentNotFoundError
from deployments.schemas import DeploymentCreate
from utils.dependency import DeploymentsServiceDep, UOWDep, UpstreamsServiceDep
from utils.exceptions import exception_handler

router = APIRouter(prefix='/deployments', tags=['Deployments'])


@router.get('/')
@exception_handler
async def get_deployments_handler(deployments_service: DeploymentsServiceDep,
                                  uow: UOWDep):
    deployments = await deployments_service.read_deployments(uow)
    return {
        'data': deployments,
        'detail': 'Deployments were selected.'
    }


@router.get('/{uuid}')
@exception_handler
async def get_deployment_handler(deployments_service: DeploymentsServiceDep,
                                 uow: UOWDep,
                                 uuid: UUID):
    deployment = await deployments_service.read_deployment(uow, uuid=uuid)
    if not deployment:
        raise DeploymentNotFoundError

    return {
        'data': deployment,
        'detail': 'Deployment was selected.'
    }


@router.post('/')
@exception_handler
async def post_deployments_handler(deployments_service: DeploymentsServiceDep,
                                   uow: UOWDep,
                                   deployment: DeploymentCreate):
    uuid = await deployments_service.create_deployment(uow, deployment)
    return {
        'data': str(uuid),
        'detail': 'Deployment was created.'
    }


@router.delete('/{uuid}')
@exception_handler
async def delete_deployment(deployment_service: DeploymentsServiceDep,
                            upstreams_service: UpstreamsServiceDep,
                            uow: UOWDep,
                            uuid: UUID):
    deployment = await deployment_service.read_deployment(uow, uuid=uuid)
    if not deployment:
        raise DeploymentNotFoundError

    upstreams = await upstreams_service.read_upstreams(uow, deployment_uuid=uuid)
    for upstream in upstreams:
        await upstreams_service.delete_upstream(uow, upstream.uuid)

    await deployment_service.delete_deployment(uow, uuid=uuid)
    return {
        'data': None,
        'detail': 'Deployment was deleted.'
    }
