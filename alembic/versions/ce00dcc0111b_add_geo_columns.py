"""Add geo columns

Revision ID: ce00dcc0111b
Revises: 59352e2efbce
Create Date: 2025-07-24 16:39:37.132499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geography

# revision identifiers, used by Alembic.
revision: str = 'ce00dcc0111b'
down_revision: Union[str, Sequence[str], None] = '59352e2efbce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('accommodations', sa.Column('geo', Geography(geometry_type='POINT', srid=4326)))
    op.add_column('attractions', sa.Column('geo', Geography(geometry_type='POINT', srid=4326)))


def downgrade() -> None:
    op.drop_column('attractions', 'geo')
    op.drop_column('accommodations', 'geo') 


