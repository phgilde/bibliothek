from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email
from isbnlib import notisbn
from wtforms import ValidationError


class NewStudentForm(FlaskForm):
    first_name = StringField("Vorname", validators=[InputRequired()])
    last_name = StringField("Nachname", validators=[InputRequired()])
    phone_number = StringField("Telefonnummer", validators=[InputRequired()])
    email = StringField("Emailadresse", validators=[InputRequired(), Email()])
    tutor = StringField("Tutor", validators=[InputRequired()])
    submit = SubmitField("Hinzufügen")


class NewBookForm(FlaskForm):
    isbn = StringField("ISBN", validators=[InputRequired()])

    def validate_isbn(form, field):
        if notisbn(field.data):
            raise ValidationError("Ungültige ISBN")

    submit = SubmitField("Hinzufügen")


class BorrowForm(FlaskForm):
    student = StringField("Schüler", validators=[InputRequired()])
    book = StringField("Buch", validators=[InputRequired()])
    submit = SubmitField("Ausleihen")
