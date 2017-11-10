from flask_wtf import FlaskForm
from wtforms import (
    StringField, HiddenField, PasswordField
)
from wtforms.validators import InputRequired


class CustomerForm(FlaskForm):
    id = HiddenField()
    email = StringField('E-mail', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    name = PasswordField('Имя', validators=[InputRequired()])
    country = PasswordField('Страна', validators=[InputRequired()])
    address = PasswordField('Адрес', validators=[InputRequired()])
