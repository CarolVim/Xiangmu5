"""empty message

Revision ID: 9f404796b7db
Revises: 
Create Date: 2021-05-30 10:17:36.707532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f404796b7db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('newspaper',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('detail', sa.String(length=255), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('addDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_newspaper_addDate'), 'newspaper', ['addDate'], unique=False)
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('apply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('applyId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('cost', sa.String(length=50), nullable=True),
    sa.Column('level', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('img', sa.String(length=255), nullable=True),
    sa.Column('zip', sa.String(length=255), nullable=True),
    sa.Column('applyDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['applyId'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apply_applyDate'), 'apply', ['applyDate'], unique=False)
    op.create_table('context',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('context', sa.String(length=255), nullable=True),
    sa.Column('addDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_context_addDate'), 'context', ['addDate'], unique=False)
    op.create_table('xiangmu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('picture', sa.String(length=255), nullable=True),
    sa.Column('detail', sa.String(length=255), nullable=True),
    sa.Column('applyId', sa.Integer(), nullable=True),
    sa.Column('applydate', sa.DateTime(), nullable=True),
    sa.Column('finishdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['applyId'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_xiangmu_applydate'), 'xiangmu', ['applydate'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_xiangmu_applydate'), table_name='xiangmu')
    op.drop_table('xiangmu')
    op.drop_index(op.f('ix_context_addDate'), table_name='context')
    op.drop_table('context')
    op.drop_index(op.f('ix_apply_applyDate'), table_name='apply')
    op.drop_table('apply')
    op.drop_table('user')
    op.drop_index(op.f('ix_newspaper_addDate'), table_name='newspaper')
    op.drop_table('newspaper')
    op.drop_table('admin')
    # ### end Alembic commands ###
