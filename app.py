from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<html> <body> <h1> Hello </h1> </body> </html>"
if __name__ == "__main__":
    app.run(debug=True)
