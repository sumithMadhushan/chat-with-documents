from flask import Flask, request
import functions

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Smart Reader API</h1>"

@app.route("/get-text-content", methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        result = functions.ExtractTextContent(f)

        return result

if __name__ == "__main__":
    app.run("localhost", 4449)
