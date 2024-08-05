from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'telnet smtp.gmail.com 587'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'itboys2023@gmail.com'
app.config['MAIL_PASSWORD'] = 'Nscetitguys2023'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send_email')
def send_email():
    msg = Message("Hello", sender="itboys2023@gmail.com", recipients=["hari54stark@gmail.com"])
    msg.body = "This is a test email."
    mail.send(msg)
    return "Email sent!"
