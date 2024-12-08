from flask import Flask, render_template

app = Flask(__name__)


sample = ["One", "Two", "Three", "Four", "Five"]


@app.route("/")
def home():
    return render_template("index.html", the_list=sample)


@app.route("/me")
def me():
    return "<h1>me</h1>"


if __name__ == "__main__":
    app.run(debug=True)
