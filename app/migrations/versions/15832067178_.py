"""empty message

Revision ID: 15832067178
Revises: 19f4a2511e1
Create Date: 2018-11-12 04:58:56.262374

"""

# revision identifiers, used by Alembic.
revision = '15832067178'
down_revision = '19f4a2511e1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracefiles', sa.Column('date_deleted', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tracefiles', 'date_deleted')
    ### end Alembic commands ###
