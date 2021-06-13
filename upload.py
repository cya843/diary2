from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

##file upload
@app.route('/upload')
def upload():
       return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
       if request.method == 'POST':
           f= request.files['file']
           if not os.path.exists("./data"):
               os.makedirs('./data')
           f.save("./data/" + secure_filename(f.filename))
           return 'file uploaded successfully!'

if __name__ == '__main__':
       app.run(debug = True)


