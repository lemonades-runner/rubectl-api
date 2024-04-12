# from pathlib import Path

from fastapi import FastAPI

# import alembic.config
# import alembic.command

from deployments.router import router as deployments_router
from upstreams.router import router as upstreams_router

from utils.config import VERSION

app = FastAPI(
    title='Rubectl API',
    version=VERSION,
    description='API for deploying Docker images to the GitHub infrastructure.'
)


@app.get(f'/', tags=['Setup'])
async def get_root_handler():
    return 'Welcome to Rubectl API! Visit /docs or /redoc for the full documentation.'


@app.get(f'/readyz', tags=['Setup'])
async def get_readyz_handler():
    return {
        'data': 'ready',
        'detail': 'Rubectl API is up and running.'
    }


@app.get(f'/healthz', tags=['Setup'])
async def get_healthz_handler():
    return {
        'data': 'health',
        'detail': 'Rubectl API is up and running.'
    }


@app.get(f'/publication/ready', tags=['Setup'])
async def get_healthz_handler():
    return {
        'data': 'publication ready',
        'detail': 'Rubectl API is up and running.'
    }


@app.get(f'/version', tags=['Setup'])
async def get_version_handler():
    return {
        'data': VERSION,
        'detail': 'Version was selected.'
    }


app.include_router(deployments_router, prefix='/api/v1')
app.include_router(upstreams_router, prefix='/api/v1')


# @app.on_event('startup')
# def startup_event():
#     try:
#         alembic_ini_path = Path(__file__).parent / 'migrations' / 'alembic.ini'
#         alembic_config = alembic.config.Config(str(alembic_ini_path))
#         alembic_config.set_main_option('sqlalchemy.url', DB_URL)
#         alembic.command.upgrade(alembic_config, 'head')
#         print('Alembic Revision Upgraded.')
#     except Exception as e:
#         print('Alembic Revision Upgrade Error:', e)
