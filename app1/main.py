from flask import Flask
app = Flask(__name__)

@app.route("/app1")
def hello():
    return "Hello from App1"