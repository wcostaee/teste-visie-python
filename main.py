from flask import Flask, url_for, render_template, redirect
from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def main():
    data = db.search_all()
    data_formatted = []
    for each in data:
        data_formatted.append(format_data(each))
    return render_template("home.html", data_formatted=data_formatted)

@app.route("/delete/<id_person>")
def delete(id_person):
    db.delete(int(id_person))
    # data = db.search_all()
    # data_formatted = []
    # for each in data:
    #     data_formatted.append(format_data(each))
    # return render_template("home.html", data=data_formatted)
    return redirect(url_for("main"))

def format_data(data):
    if len(data) == 3:
        if data[1] is None: #O nome é NULL no banco de dados
            name = "-"
        else:
            name = (str(data[1])).split()[0]
        if data[2] is None:
            date = "Indefinido"
        else:
            temp = (str(data[2])).split("-")
            if len(temp) == 3:
                date = temp[2] + "/" + temp[1] + "/" + temp[0]
            else:
                date = "Indefinido"
        info_output = (data[0], name, date)
        return info_output

# @app.route("/style.css")
# def static_css():
#     return url_for("static", filename="style.css")