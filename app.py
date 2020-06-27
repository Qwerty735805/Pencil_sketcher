import os
from flask import Flask, send_from_directory
from flask import render_template, request
import sketch
import imutils
import cv2

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def run():
    image_path = "static/content.jpg"

    s = sketch.load_img(image_path)
    final=sketch.convert(s)
    cv2.imwrite("static/output.jpg",final)
    # cv2.imwrite("images/output/output.jpg", img)

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    target = os.path.join(APP_ROOT, 'static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    # file_name=""
    for file in request.files.getlist("file"):
        print(file)
        destination = "/".join([target, "content.jpg"])
        print(destination)
        file.save(destination)
    run()

    file_name="output.jpg"
    return render_template("output.html", image_name=file_name)
    # return send_from_directory("images/output", file_name, as_attachment=True)


@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images/output", filename)


if __name__ == "__main__":
    app.run(debug=False)