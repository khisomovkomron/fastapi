"""crete phone number for user column

Revision ID: 4df1a03d19af
Revises: 
Create Date: 2022-11-02 22:23:33.752713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df1a03d19af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
