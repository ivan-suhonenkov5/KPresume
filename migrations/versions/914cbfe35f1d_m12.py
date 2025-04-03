"""m12

Revision ID: 914cbfe35f1d
Revises: d1d0a1e26abe
Create Date: 2025-03-21 16:14:22.856185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '914cbfe35f1d'
down_revision = 'd1d0a1e26abe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
