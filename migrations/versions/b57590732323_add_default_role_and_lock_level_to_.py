"""Add default_role and lock_level to Channel

Revision ID: b57590732323
Revises: fbf90b8f8171
Create Date: 2020-11-03 20:27:53.805409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b57590732323'
down_revision = 'fbf90b8f8171'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('default_role', sa.BigInteger(), nullable=True))
    op.add_column('channels', sa.Column('lock_level', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'channels', 'roles', ['default_role'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channels', type_='foreignkey')
    op.drop_column('channels', 'lock_level')
    op.drop_column('channels', 'default_role')
    # ### end Alembic commands ###
