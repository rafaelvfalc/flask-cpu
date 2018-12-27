import psutil

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ""

@app.route("/cpu")
def get_cpu():
    return str(psutil.cpu_percent()/100.0)

if __name__ == "__main__":
    app.run(debug=True)