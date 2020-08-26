from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="yourusername",
    password="yourpassword",
    hostname="thehostname",
    databasename="yourdbname",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Poetry(db.Model):

    __tablename__ = "poetries"

    id = db.Column(db.Integer, primary_key=True)
    verse = db.Column(db.String(4096))
    author = db.Column(db.String(4096))

class PoetrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Poetry
        load_instance = True

@app.route('/')
def index():
    number = random.randint(1,4)
    aPoetry = Poetry.query.filter_by(id=number).first()
    poetry_schema = PoetrySchema(many=False)
    output = poetry_schema.dump(aPoetry)
    return render_template("main_page.html", poetry = output)

@app.route('/verse/', methods=["GET","POST"])
def poetry():
    if request.method == "GET":
        number = random.randint(1,4)
        aPoetry = Poetry.query.filter_by(id=number).first()
        poetry_schema = PoetrySchema(many=False)
        output = poetry_schema.dump(aPoetry)
        return {'poetry' : output}

    poetries = Poetry(verse=request.form["contents"], author=request.form["authorName"])
    db.session.add(poetries)
    db.session.commit()
    return redirect(url_for('index'))
