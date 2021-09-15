"""deleted registered on

Revision ID: c723efeea219
Revises: 8b8700623d2f
Create Date: 2021-08-30 23:01:49.780602

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c723efeea219'
down_revision = '8b8700623d2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('ix_users_updated_at'), 'users', ['updated_at'], unique=False)
    op.drop_column('users', 'registered_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('registered_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_users_updated_at'), table_name='users')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    # ### end Alembic commands ###