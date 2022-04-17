import os
from flask import render_template, request
from api import app
from api.helper import conversion_logic

app_path = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/index", methods=['GET', 'POST'])
def upload():
    target = os.path.join(app_path, 'example_files/')
    output_format = request.form.get('dropdown')
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        filename = file.filename
        last_ext = os.path.splitext(filename)[1]
        if last_ext not in ['.jpg', '.png', '.bmp', '.ppm', '.gif', '.tiff', '.pdf']:
            return render_template('error.html')

        else:
            upload.destination = "/".join([target, filename])
            conversion_logic(upload.destination, output_format)
            return render_template('complete.html')
