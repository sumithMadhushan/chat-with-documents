import glob
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import functions
import json
import answers

app = Flask(__name__)

fileTextContent = None  # Global variable to store the imported file content
uploadeFileName = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload():
    # Access the global content variable
    global fileTextContent
    global uploadeFileName

    if request.method == "POST":
        if fileTextContent:
            content = fileTextContent
        else:
            f = request.files["file"]
            filename = secure_filename(f.filename)
            fileContent = functions.ExtractTextContent(f)
            stringResult = json.loads(fileContent)
            content = stringResult["data"]
            fileTextContent = content
            uploadeFileName = filename

        # Prompt for user question from UI
        question = request.form.get("question")

        # Use ML trained models from the tensorflow to get the answers
        if "summar" in question.lower():
            answer = answers.summarizer(content)
        else:
            answer = answers.answer_question(content, question)

        return render_template(
            "question.html", answer=answer, uploadedFileName=uploadeFileName
        )


if __name__ == "__main__":
    app.run("localhost", 4449)
