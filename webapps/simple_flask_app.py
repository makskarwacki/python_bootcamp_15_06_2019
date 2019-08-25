from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return render_template('test.html', name=name)

if __name__ == "__main__":
    app.run()