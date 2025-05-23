from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html") 

@app.route("/mhw")
def mhw():
    return render_template("mhw.html")

@app.route("/from")
def from_page():
    return render_template("from.html")

@app.route("/bik")
def bik():
    return render_template("bik.html")

@app.route("/turi")
def turi():
    return render_template("turi.html")

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)
