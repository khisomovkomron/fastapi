"""add apt num col

Revision ID: c1434c299443
Revises: 9e99c56556c9
Create Date: 2022-11-02 23:09:21.713385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1434c299443'
down_revision = '9e99c56556c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
