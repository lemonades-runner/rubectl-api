"""initial

Revision ID: 09dadf6bf4e5
Revises: 
Create Date: 2024-04-12 18:25:35.784967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09dadf6bf4e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deployment',
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('upstream',
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('deployment_uuid', sa.Uuid(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_uuid'], ['deployment.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upstream')
    op.drop_table('deployment')
    # ### end Alembic commands ###
