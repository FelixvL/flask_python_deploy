from flask import Flask, render_template
from .bestand1 import *

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/een")
def methodeEen():
    terug = eenmethodeinbestand1()
    return "methodeeen" + terug

#@app.route("/twee")
#def methodeTwee():
#    terug = been.methodeMetReadFile()
#    return "methodeEen"+terug

