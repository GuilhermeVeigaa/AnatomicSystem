"""empty message

Revision ID: 2a25668585ba
Revises: 
Create Date: 2022-12-02 01:49:25.628551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a25668585ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('peças',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('alunos',
    sa.Column('matricula', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('curso_nome', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['curso_nome'], ['cursos.nome'], ),
    sa.PrimaryKeyConstraint('matricula')
    )
    op.create_table('reservas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('aluno_matricula', sa.Integer(), nullable=True),
    sa.Column('peca_nome', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['aluno_matricula'], ['alunos.matricula'], ),
    sa.ForeignKeyConstraint(['peca_nome'], ['peças.nome'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservas')
    op.drop_table('alunos')
    op.drop_table('peças')
    op.drop_table('cursos')
    # ### end Alembic commands ###