from flask import Flask

app = Flask(__name__)

@app.route("/")
def saynotociggarates():
    return "<a href='https://www.google.com/maps'>Ciggarates is injurious to health</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
