"""empty message

Revision ID: 55f06c828437
Revises: 2c856669b85b
Create Date: 2017-03-10 00:02:00.396448

"""

# revision identifiers, used by Alembic.
revision = '55f06c828437'
down_revision = '2c856669b85b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DATETIME(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
