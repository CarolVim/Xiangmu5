"""empty message

Revision ID: b99f69addc12
Revises: 7e3b0a57807d
Create Date: 2021-05-31 09:40:24.566118

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b99f69addc12'
down_revision = '7e3b0a57807d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('answer', sa.String(length=255), nullable=True),
    sa.Column('addDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_addDate'), 'record', ['addDate'], unique=False)
    op.drop_index('ix_context_addDate', table_name='context')
    op.drop_table('context')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('context',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('userId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('context', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('addDate', mysql.DATETIME(), nullable=True),
    sa.Column('status', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.uid'], name='context_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_context_addDate', 'context', ['addDate'], unique=False)
    op.drop_index(op.f('ix_record_addDate'), table_name='record')
    op.drop_table('record')
    # ### end Alembic commands ###
