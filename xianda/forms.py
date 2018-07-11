__author__ = 'xianda'
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from models import Article
from extends import db


class ArticleForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    author = StringField('作者', validators=[DataRequired()])
    tag = StringField('类型', validators=[DataRequired()])
    submit = SubmitField('提交')

    def create_article(self):
        article = Article()
        self.populate_obj(article)
        db.session.add(article)
        db.session.commit()
        return article

    def update_article(self, article):
        self.populate_obj(article)
        db.session.add(article)
        db.session.commit()
        return article
