"""create address table

Revision ID: 7882bdccb75e
Revises: 4df1a03d19af
Create Date: 2022-11-02 22:31:33.019656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7882bdccb75e'
down_revision = '4df1a03d19af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
