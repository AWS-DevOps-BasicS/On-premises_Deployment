from flask import Flask
app = Flask(__name__)

@app.route("/app2")
def hello():
    return "Hello from App2"