import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# specify the types of allowed file formats and the max size
ALLOWED_EXTENSIONS = {'doc','xls','pdf'}
MAX_CONTENT_LENGTH = 1* 1024 * 1024 

app=Flask(__name__)
# specify the maximum allowed payload to 1 megabytes
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# creating a function to check if the loaded file is eligible
def allowed_file_type(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


# Creating the Index page
@app.route('/')
def index_page():
    return render_template('index_page.html')

# Creating the Uploader page (Local hosted API)
@app.route('/Phuong_uploader', methods=['GET', 'POST'])
def upload_page_local():
    if request.method == 'POST':
        
        file = request.files['file']
        
        # check if no file is selected/file has no name , a warnming message will be generated to remind
        if file.filename == '':
            return render_template('NoFileSelect.html') 
        
        
        # check if the type of file extension is eligible, load it
        if file and allowed_file_type(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            return render_template('SucessNotice.html')  
            
        else:
            return render_template('WrongFileSelect.html') 
            
    return render_template('upload_page_local.html') 

# Creating the Uploader page (AWS hosted API)
@app.route('/beta/upload', methods=['GET', 'POST'])
def upload_page_AWS():
    if request.method == 'POST':
        
        file = request.files['file']
        
        # check if no file is selected/file has no name , a warnming message will be generated to remind
        if file.filename == '':
            return render_template('NoFileSelect.html') 
        
        # check if the type of file extension is eligible, load it
        if file and allowed_file_type(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            return render_template('SucessNotice.html')  
            
        else:
            return render_template('WrongFileSelect.html') 
            
    return render_template('upload_page_AWS.html') 

# Creating a page of conclusion
@app.route('/conclusion_page', methods=['GET', 'POST'])
def conclusion_page():
    return render_template('conclusion_page.html')

if __name__ == "__main__":
    app.run()