from flask import Flask, render_template
#from externebestanden import bestand1 as been

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")



