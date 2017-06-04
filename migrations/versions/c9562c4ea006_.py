"""empty message

Revision ID: c9562c4ea006
Revises: 1596dba0dc7f
Create Date: 2017-06-04 19:42:36.924742

"""

# revision identifiers, used by Alembic.
revision = 'c9562c4ea006'
down_revision = '1596dba0dc7f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('projected_date', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'projected_date')
    ### end Alembic commands ###