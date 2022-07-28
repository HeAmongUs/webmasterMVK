from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/convertToPng")
def convert_to_png():
    return "<p>Hello, World!</p>"

@app.route("/convertToJpg")
def convert_to_jph():
    return "<p>Hello, World!</p>"

@app.route("/convertToBmp")
def convert_to_bmp():
    return "<p>Hello, World!</p>"\

@app.route("/convertToSvg")
def convert_to_svg():
    return "<p>Hello, World!</p>"