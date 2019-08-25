from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/")
def index():
    return "Hello Flask!!"

@app.route("/helloworld")
def index2():
    return "Hello World!!"

@app.route("/hello/<string:name>")
def hello_name(name):
    return render_template("hello.html", name=name, x=12,
                           products = ["a", "b", "c"]
                           )


if __name__ == "__main__":
    app.run()