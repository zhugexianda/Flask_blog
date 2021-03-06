"""empty message

Revision ID: 924c23aab8a1
Revises: 1e1b08096d17
Create Date: 2018-05-21 10:53:43.765377

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '924c23aab8a1'
down_revision = '1e1b08096d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info')
    op.add_column('article', sa.Column('tag', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'tag')
    op.create_table('info',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('me', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
