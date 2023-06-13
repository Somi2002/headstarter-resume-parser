from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from firebase_service import initialize_firebase, save_resume, search_resumes
import PyPDF2
import docx
from flask import send_from_directory
import logging
from flask_login import UserMixin
from flask_login import LoginManager
from flask_login import login_user, current_user, login_required
from flask_login import logout_user
from flask import redirect, url_for, flash
from flask_login import login_required

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './resumes'

app.config['SECRET_KEY'] = 'your_secret_key_here'
login_manager = LoginManager(app)

# Initialize Firebase
initialize_firebase()

class Admin(UserMixin):
    def get_id(self):
        return 'admin'

@login_manager.user_loader
def load_user(user_id):
    if user_id == 'admin':
        return Admin()
    return None

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        passcode = request.form.get('passcode')
        if passcode == 'headstarter':
            user = Admin()
            login_user(user)
            return redirect(url_for('search'))
        else:
            flash('Invalid passcode.', 'error')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Functions to extract text
def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""
    for page_num in range(len(pdf_reader.pages)): 
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return 'No file part'
    file = request.files['resume']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension == '.pdf':
            try:
                text = extract_text_from_pdf(file_path)
            except Exception as e:
                return 'Error extracting text from PDF: {}'.format(e)
        elif file_extension == '.docx':
            try:
                text = extract_text_from_docx(file_path)
            except Exception as e:
                return 'Error extracting text from DOCX: {}'.format(e)
        else:
            return 'Unsupported file type'
        resume_data = {'text': text, 'id': filename}
        save_resume(resume_data)
        return 'Resume saved.'

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        results = search_resumes(keyword)
        return render_template('search_results.html', results=results)
    else:
        return render_template('search_results.html', results=[])

if __name__ == '__main__':
    app.run(debug=True)

