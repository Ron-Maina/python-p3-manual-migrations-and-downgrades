"""Renaming students to scholars

Revision ID: 542969b25815
Revises: 791279dd0760
Create Date: 2023-08-29 17:10:29.995060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542969b25815'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass

def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass