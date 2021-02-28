from flask import Flask, url_for, render_template
from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def main():
    registros = db.search_all()
    return render_template("home.html", registros=registros)

# @app.route("/style.css")
# def static_css():
#     return url_for("static", filename="style.css")