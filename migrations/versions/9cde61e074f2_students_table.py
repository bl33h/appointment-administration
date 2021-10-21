"""Students Table

Revision ID: 9cde61e074f2
Revises: 1dd24ecf417b
Create Date: 2021-10-21 15:33:26.974653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cde61e074f2'
down_revision = '1dd24ecf417b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudiante',
    sa.Column('carne', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=64), nullable=True),
    sa.Column('carrera', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('carne')
    )
    op.create_index(op.f('ix_estudiante_carrera'), 'estudiante', ['carrera'], unique=False)
    op.create_index(op.f('ix_estudiante_nombre'), 'estudiante', ['nombre'], unique=False)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.drop_index(op.f('ix_estudiante_nombre'), table_name='estudiante')
    op.drop_index(op.f('ix_estudiante_carrera'), table_name='estudiante')
    op.drop_table('estudiante')
    # ### end Alembic commands ###
