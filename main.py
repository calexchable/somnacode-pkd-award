from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://pkd-award:password@localhost:8889/pkd-award"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

class Winners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    book_title = db.Column(db.String(120))

    def __init__(self, year, first_name, last_name, book_title):
        self.year = year
        self.first_name = first_name
        self.last_name = last_name
        self.book_title = book_title

class Nominees(db.Model):
    

@app.route("/")
def index():
    return "Somnacode presents: The Philip K Dick Award APP"

@app.route("/update", methods=["POST", "GET"])
def award_update():
    if request.method == "POST":
        year = request.form["year"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        book_title = request.form["book_title"]

        new_data = Winners(year, first_name, last_name, book_title)

        db.session.add(new_data)
        db.session.commit()

    return render_template("update.html")

if __name__ == "__main__":
    app.run()