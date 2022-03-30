from flask import (
    flash,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from app import app, db
from app.forms import NewStudentForm, NewBookForm
from app.models import Book, Student
import json
from urllib.parse import quote


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/newstudent", methods=["GET", "POST"])
def new_student():
    form = NewStudentForm()
    if form.validate_on_submit():
        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data,
            email=form.email.data,
            tutor=form.tutor.data,
        )
        db.session.add(student)
        db.session.commit()

        flash("Erfolgreich Hinzugefügt")
        return make_response(redirect(url_for("new_student")))
    return render_template("new_student.html", form=form)


@app.route("/newbook", methods=["GET", "POST"])
def new_book():
    form = NewBookForm()
    if form.validate_on_submit():
        book = Book(
            isbn=form.isbn.data,
            is_borrowed=False,
        )
        db.session.add(book)
        db.session.commit()

        flash("Erfolgreich Hinzugefügt")
        return make_response(redirect(url_for("new_book")))
    return render_template("new_book.html", form=form)
