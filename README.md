# headstarter-resume-parser

Resume Parser is a web application that allows users to upload resumes in PDF or DOCX format and extracts relevant information such as contact details, skills, education, work experience, and more. The extracted information can be used for various purposes, including job matching, talent acquisition, and resume analysis.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Resume upload: Users can upload resumes in PDF or DOCX format.
- Text extraction: The application extracts text from the uploaded resumes using PyPDF2 for PDF files and python-docx for DOCX files.
- Information extraction: The extracted text is processed to extract relevant information such as contact details, skills, education, work experience, etc.
- Firebase integration: The application uses Firebase Firestore to store the extracted resume data.
- Search functionality: Users can search for resumes based on keywords, such as skills or job titles.
- User authentication: The application includes a login system with admin access for managing resumes and search functionality.

## Technologies Used

- Python
- Flask
- PyPDF2
- python-docx
- Firebase Firestore
- HTML/CSS
- JavaScript

## Getting Started

### Prerequisites

- Python 3.7 or above
- pip package manager
- Firebase project with Firestore enabled

### Installation

1. Clone the repository:

2. Navigate to the project directory:


3. Install the required dependencies:


4. Set up your Firebase project and obtain the Firebase admin SDK JSON file.

5. Move the Firebase admin SDK JSON file to the project directory.

### Configuration

1. Open `firebase_service.py` and replace the path to your Firebase admin SDK JSON file:

```python
cred = credentials.Certificate('path/to/your/firebase-adminsdk.json')
app.config['SECRET_KEY'] = 'your_secret_key_here'
firebase_admin.initialize_app(cred, {'projectId': 'your-project-id'})

Usage
1. Start the application:
   python app.py
   
2. Open your web browser and navigate to http://localhost:5000.

3. Use the provided login system to log in as an admin.

4. Upload resumes in PDF or DOCX format using the upload form.

5. Search for resumes using keywords.

6. Explore the extracted information and analyze the resume data.

Contributing
Contributions to the Resume Parser project are welcome! If you encounter any bugs, issues, or have suggestions for improvements, please feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License.
