from flask import render_template
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os

from models.model import predict_human_dog
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# source: https: // flask.palletsprojects.com/en/1.1.x/patterns/fileuploads /?highlight = javascript


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# route for prediction

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            img_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # predict function
            prediction = predict_human_dog(img_file_path)
            # delete uploaded file
            os.remove(img_file_path)
            return jsonify(prediction)
        # return True

    return "ooooooppppppssss"
