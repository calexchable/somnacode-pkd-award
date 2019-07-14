from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return "Somnacode presents: The Philip K Dick Award APP"

app.run()