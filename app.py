from flask import Flask, render_template, request
from externebestanden import bestand1 as been

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/een")
def methodeEen():
    terug = been.eenmethodeinbestand1()
    return "methodeeen "+terug

@app.route("/twee")
def methodeTwee():
    terug = been.methodeMetReadFile()
    return "methodeEen"+terug

if __name__ == '__main__':
    app.run(debug=True)