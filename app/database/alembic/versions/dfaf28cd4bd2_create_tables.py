"""create tables

Revision ID: dfaf28cd4bd2
Revises: 
Create Date: 2021-02-12 14:01:10.243130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfaf28cd4bd2'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'Civilizations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=True),
        sa.Column('expansion', sa.String(50), nullable=True)
    )

def downgrade():
    op.drop_table('Civilizations')