"""create city, attraction, accommodation, search  table

Revision ID: 59352e2efbce
Revises: da9415c179aa
Create Date: 2025-07-23 18:05:27.553289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59352e2efbce'
down_revision: Union[str, Sequence[str], None] = 'da9415c179aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cities_country'), 'cities', ['country'], unique=False)
    op.create_index(op.f('ix_cities_id'), 'cities', ['id'], unique=False)
    op.create_index(op.f('ix_cities_name'), 'cities', ['name'], unique=False)
    op.create_table('accommodations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('number_of_reviews', sa.Integer(), nullable=True),
    sa.Column('amenities', sa.JSON(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accommodations_id'), 'accommodations', ['id'], unique=False)
    op.create_index(op.f('ix_accommodations_name'), 'accommodations', ['name'], unique=False)
    op.create_table('attractions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('popularity', sa.Float(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_attractions_category'), 'attractions', ['category'], unique=False)
    op.create_index(op.f('ix_attractions_id'), 'attractions', ['id'], unique=False)
    op.create_index(op.f('ix_attractions_name'), 'attractions', ['name'], unique=False)
    op.create_table('user_searches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('selected_attraction_ids', sa.JSON(), nullable=True),
    sa.Column('budget_min', sa.Float(), nullable=True),
    sa.Column('budget_max', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_searches_id'), 'user_searches', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_searches_id'), table_name='user_searches')
    op.drop_table('user_searches')
    op.drop_index(op.f('ix_attractions_name'), table_name='attractions')
    op.drop_index(op.f('ix_attractions_id'), table_name='attractions')
    op.drop_index(op.f('ix_attractions_category'), table_name='attractions')
    op.drop_table('attractions')
    op.drop_index(op.f('ix_accommodations_name'), table_name='accommodations')
    op.drop_index(op.f('ix_accommodations_id'), table_name='accommodations')
    op.drop_table('accommodations')
    op.drop_index(op.f('ix_cities_name'), table_name='cities')
    op.drop_index(op.f('ix_cities_id'), table_name='cities')
    op.drop_index(op.f('ix_cities_country'), table_name='cities')
    op.drop_table('cities')
    # ### end Alembic commands ###
