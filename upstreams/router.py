from uuid import UUID

from fastapi import APIRouter

from upstreams.exceptions import UpstreamNotFoundError
from upstreams.schemas import UpstreamCreate
from utils.dependency import UpstreamsServiceDep, UOWDep
from utils.exceptions import exception_handler

router = APIRouter(prefix='/upstreams', tags=['Upstreams'])


@router.get('/')
@exception_handler
async def get_upstreams_handler(upstreams_service: UpstreamsServiceDep,
                                uow: UOWDep,
                                deployment_uuid: str | None = None):
    upstreams = await upstreams_service.read_upstreams(uow, deployment_uuid=deployment_uuid)
    return {
        'data': upstreams,
        'detail': 'Upstreams were selected.'
    }


@router.get('/{uuid}')
@exception_handler
async def get_upstream_handler(upstreams_service: UpstreamsServiceDep,
                               uow: UOWDep,
                               uuid: UUID):
    upstream = await upstreams_service.read_upstream(uow, uuid=uuid)
    if not upstream:
        raise UpstreamNotFoundError

    return {
        'data': upstream,
        'detail': 'Upstream was selected.'
    }


@router.post('/')
@exception_handler
async def post_upstreams_handler(upstreams_service: UpstreamsServiceDep,
                                 uow: UOWDep,
                                 upstream: UpstreamCreate):
    uuid = await upstreams_service.create_upstream(uow, upstream)
    return {
        'data': str(uuid),
        'detail': 'Upstream was created.'
    }


@router.delete('/{uuid}')
@exception_handler
async def delete_upstream(upstream_service: UpstreamsServiceDep,
                          uow: UOWDep,
                          uuid: UUID):
    upstream = await upstream_service.read_upstream(uow, uuid=uuid)
    if not upstream:
        raise UpstreamNotFoundError

    await upstream_service.delete_upstream(uow, uuid=uuid)
    return {
        'data': None,
        'detail': 'Upstream was deleted.'
    }
