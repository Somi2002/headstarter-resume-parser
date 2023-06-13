import PyPDF2
from docx import Document
import re
import spacy

nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(filename):
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ' '.join([page.extract_text() for page in pdf_reader.pages])
    pdf_file.close()
    return text

def extract_text_from_docx(filename):
    doc = Document(filename)
    return ' '.join([p.text for p in doc.paragraphs])

def extract_email(text):
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return email

def extract_mobile_number(text):
    phone = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return phone

def extract_skills(text):
    skills = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL",
              "Communication", "Teamwork", "Creativity", "Project Management"]
    present_skills = [skill for skill in skills if skill in text]
    return present_skills

def extract_total_experience(text):
    years = re.findall(r'\d+\s*(?:years|yrs)', text, re.I)
    return years

def extract_education(text):
    education = re.findall(r'\b(?:B\.?A\.?|B\.?S\.?|M\.?A\.?|M\.?S\.?|Ph\.?D\.?)\b[\s\w,]*(?:from|at)\s[\w\s]*', text, re.I)
    return education

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return None

def extract_designation(text):
    designation = re.findall(r'(?:as|role)[\s\w]*(?:at)', text, re.I)
    return designation

def extract_company_names(text):
    doc = nlp(text)
    companies = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    return companies
