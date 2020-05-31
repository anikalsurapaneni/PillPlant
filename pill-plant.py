# import the Flask class from the flask module
from flask import Flask, flash, render_template, url_for, request, redirect
import urllib.request
from werkzeug.utils import secure_filename
from livereload import Server
import os
from PIL import Image

UPLOAD_FOLDER = 'static/uploads/'

# create the application object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/")
def welcome():
    return render_template("tums.html")  # render a template

@app.route("/product")
def product():
    return render_template("product.html") 

@app.route("/pill-plant")
def pillplant():
    return render_template("home.html") 

@app.route("/problem")
def problem():
    return render_template("home.html") 


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/scan')
def upload_form():
	return render_template('scan.html')

@app.route('/scan', methods=['GET','POST'])
def upload_image():
		return render_template('tums.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'