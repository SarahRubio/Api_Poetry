from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="##",
    password="##",
    hostname="apiPoetry.mysql.pythonanywhere-services.com",
    databasename="##",
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


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        allPoetries = Poetry.query.all()
        poetry_schema = PoetrySchema(many=True)
        output = poetry_schema.dump(allPoetries)
        return {'poetries' : output}

    poetries = Poetry(verse=request.form["contents"], author=request.form["authorName"])
    db.session.add(poetries)
    db.session.commit()
    return redirect(url_for('index'))

