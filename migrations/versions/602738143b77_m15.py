"""m15

Revision ID: 602738143b77
Revises: 69232e84e932
Create Date: 2025-03-23 15:14:47.282662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602738143b77'
down_revision = '69232e84e932'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.drop_column('order')

    # ### end Alembic commands ###
