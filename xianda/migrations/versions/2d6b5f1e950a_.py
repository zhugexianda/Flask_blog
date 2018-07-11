"""empty message

Revision ID: 2d6b5f1e950a
Revises: 924c23aab8a1
Create Date: 2018-05-21 20:39:19.791571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d6b5f1e950a'
down_revision = '924c23aab8a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'name')
    # ### end Alembic commands ###
