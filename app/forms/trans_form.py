from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from app.models import Translation

class TransForm(FlaskForm):
    translation = TextAreaField('translation', validators=[DataRequired()])