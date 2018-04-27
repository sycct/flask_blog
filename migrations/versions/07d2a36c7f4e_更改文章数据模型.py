"""更改文章数据模型

Revision ID: 07d2a36c7f4e
Revises: bac6dcae778e
Create Date: 2018-04-27 21:43:43.968687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d2a36c7f4e'
down_revision = 'bac6dcae778e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('authorId', sa.Integer(), nullable=True))
    op.add_column('topics', sa.Column('picUrl', sa.String(length=200), nullable=True))
    op.add_column('topics', sa.Column('tagId', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'topics', type_='foreignkey')
    op.create_foreign_key(None, 'topics', 'tags', ['tagId'], ['id'])
    op.drop_column('topics', 'pic_url')
    op.drop_column('topics', 'tag_id')
    op.drop_column('topics', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('author_id', sa.INTEGER(), nullable=True))
    op.add_column('topics', sa.Column('tag_id', sa.INTEGER(), nullable=True))
    op.add_column('topics', sa.Column('pic_url', sa.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'topics', type_='foreignkey')
    op.create_foreign_key(None, 'topics', 'tags', ['tag_id'], ['id'])
    op.drop_column('topics', 'tagId')
    op.drop_column('topics', 'picUrl')
    op.drop_column('topics', 'authorId')
    # ### end Alembic commands ###
