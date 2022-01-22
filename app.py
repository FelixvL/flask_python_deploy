from flask import Flask, render_template, request
#from externebestanden import bestand1 as been

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")



