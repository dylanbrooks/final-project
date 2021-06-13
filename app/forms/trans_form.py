from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired
from app.models import Translation


class TransForm(FlaskForm):
    translation = StringField('translation', validators=[DataRequired()])
    startIndex = IntegerField('startIndex', validators=[DataRequired()])
    stopIndex = IntegerField('stopIndex', validators=[DataRequired()])
    userId = IntegerField('userId', validators=[DataRequired()])
    songId = IntegerField('songId', validators=[DataRequired()])

