from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    first_name = StringField('First_name', [validators.Length(min=4, max=15)])
    last_name = StringField('Last_name', [validators.Length(min=4, max=15)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
    ])