from flask import Flask, render_template
from main import *
from upload_on_flask import *


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    file_path = upload_file()
    result = number_plate_detection(file_path)
    return result

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug= False)

