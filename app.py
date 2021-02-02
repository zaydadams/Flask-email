from flask import render_template, Flask, request
import flask 

app = Flask(__name__)

@app.route('/form', method=['POST', 'GET'])
def form():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    reciever_email_id = 'zaynmr34@gmail.com'
    s.starttls()
    return render_template('contact.html')