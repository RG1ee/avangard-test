"""username field unique constraint

Revision ID: 5c30f457dd89
Revises: 881fee453414
Create Date: 2023-10-17 18:59:50.045841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5c30f457dd89"
down_revision = "881fee453414"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ["username"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="unique")

    # ### end Alembic commands ###
