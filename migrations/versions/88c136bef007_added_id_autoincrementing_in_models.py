"""added id autoincrementing in models

Revision ID: 88c136bef007
Revises: 9b6d40cba31e
Create Date: 2024-08-22 14:20:04.211312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88c136bef007'
down_revision: Union[str, None] = '9b6d40cba31e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
