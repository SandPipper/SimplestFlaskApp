from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class SimpleForm(FlaskForm):
    inputer = StringField('inputer', validators=[DataRequired(),
                                                 Length(min=2, max=20)])
