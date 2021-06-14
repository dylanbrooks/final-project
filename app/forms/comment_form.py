from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    userId = IntegerField('userId', validators=[DataRequired()])
    songId = IntegerField('songId', validators=[DataRequired()])
