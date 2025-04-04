"""m11

Revision ID: d1d0a1e26abe
Revises: e64eddbc5af5
Create Date: 2025-03-17 19:18:43.824400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d0a1e26abe'
down_revision = 'e64eddbc5af5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('file_url', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('content_category', sa.String(length=50), nullable=True))
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_column('content_category')
        batch_op.drop_column('file_url')
        batch_op.drop_column('url')

    # ### end Alembic commands ###
