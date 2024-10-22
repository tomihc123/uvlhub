"""create_notepad_model

Revision ID: d346296d9634
Revises: 001
Create Date: 2024-10-22 21:44:13.228858

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd346296d9634'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('webhook')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('webhook',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###