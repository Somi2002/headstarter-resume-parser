# firebase_service.py
import firebase_admin
import string
import logging
import re
from firebase_admin import credentials
from firebase_admin import firestore

def initialize_firebase():
    cred = credentials.Certificate(r"C:\Users\sazid\OneDrive\Desktop\Resume Parser Project\resumeparser-4eb4d-firebase-adminsdk-jt5ou-103821f404.json")
    firebase_admin.initialize_app(cred)

def custom_split(text):
    text = re.sub(r'(?<=[a-zA-Z])/(?=[a-zA-Z])', ' ', text)  # Split words separated by '/'
    words = re.findall(r'\b\w+\b', text)  # Split words at word boundaries
    return words

def save_resume(resume_data):
    db = firestore.client()
    doc_ref = db.collection('resumes').document(resume_data['id'])
    words = custom_split(resume_data['text'].lower())
    resume_data['words'] = words
    logging.info(f'Saved words: {words}')
    doc_ref.set(resume_data)

def search_resumes(keyword):
    db = firestore.client()
    resumes = db.collection('resumes').stream()
    results = []
    for resume in resumes:
        resume_dict = resume.to_dict()
        print(f"Resume ID: {resume.id}")
        print(f"Resume Data: {resume_dict}")
        if resume_dict is not None:
            if 'words' in resume_dict and isinstance(resume_dict['words'], list):
                if keyword is not None and isinstance(keyword, str) and keyword.lower() in resume_dict['words']:
                    results.append(resume_dict)
                else:
                    print(f"Invalid keyword: {keyword}")
            else:
                print(f"Missing 'words' key or invalid data in resume: {resume.id}")
        else:
            print(f"Invalid resume data for ID: {resume.id}")
    print(f"Search results for '{keyword}': {results}")
    return results







