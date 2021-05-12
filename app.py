from flask import Flask, render_template
import datetime
app = Flask(__name__)

#index page
@app.route("/index")
@app.route("/")
def index():
    return "hello"

@app.route("/Jai")
def jai():
    return "hello jai"

# @app.route("/<string:name>")
# def name(name):
#     return render_template("hello.html", name = name)

@app.route("/is<string:day>")
def dateCheck(day):
    day=day.capitalize()
    now = datetime.datetime.now()
    #return str(now)
    if now.strftime("%A") == day:
        return render_template("day.html", day=day)
    else:
        return "No"

@app.route("/hellov2")
def hellov2():
    return render_template("hello.html")

@app.route("/up")
def UP():
    return render_template("up.html")