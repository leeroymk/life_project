from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ButtonsForm(FlaskForm):
    width_form = StringField('Длина', validators=[InputRequired()])
    height_form = StringField('Высота', validators=[InputRequired()])
    submit_button = SubmitField('Создать особую жизнь')
