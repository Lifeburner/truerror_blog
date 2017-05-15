import os
import urlparse
from main import app
from flask_sqlalchemy import SQLAlchemy


urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

app.config["SQLALCHEMY_DATABASE_URI"] = url

db = SQLAlchemy(app)

class Entry(db.Model):
    primary_id = db.Column("id", db.Integer, primary_key = True)
    title = db.Column("title", db.String(120))
    content = db.Column("content", db.Text)
    time = db.Column("time", db.DateTime)