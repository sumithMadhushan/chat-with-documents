from werkzeug.utils import secure_filename
import textract
import PyPDF2
import pytesseract
from PIL import Image
import json


def ExtractTextContent(file):
    f = file
    # Save the uploaded file
    filename = secure_filename(f.filename)
    f.save(filename)

    # Read the content of the uploaded file with the correct encoding
    content = ""
    file_extension = filename.rsplit(".", 1)[1].lower()

    if file_extension == "pdf":
        with open(filename, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                # Extract the text from the page
                content += pdf_reader.pages[page_num].extract_text().lower()

    elif file_extension == "txt":
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    elif file_extension == "docx":
        content = textract.process(filename).decode("utf-8")
    elif file_extension in ["jpg", "jpeg", "png", "bmp", "gif"]:
        image = Image.open(filename)
        content = pytesseract.image_to_string(image)

    response = {
        "fileName": filename,
        "extension": file_extension,
        "characters": len(content),
        "data": content.replace("\n", "").replace("\u00a0", " "),
    }

    return json.dumps(response)
