from threading import Thread
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
app.debug=True
app.config["MAIL_SERVER"] = "smtp.qq.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "2364839934@qq.com"
app.config["MAIL_PASSWORD"] = "oycimssoihqkdhie"

mail = Mail(app)

@app.route("/send_mail")
def send_mail():
    message = Message("title",sender=app.config["MAIL_USERNAME"],recipients=["2364839934@qq.com"])
    message.body = "content"
    t = Thread(target=_send_email,args=(message,))
    t.start()
    return "succ"

def _send_email(msg):
    with app.app_context():
        mail.send(msg)

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)
    pass

'''
sender = '2364839934@qq.com'
receiver = sender
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = sender
password = 'oycimssoihqkdhie'
msg = MIMEText( 'Hello Python', 'text', 'utf-8' )
msg['Subject'] = Header( subject, 'utf-8' )
smtp = smtplib.SMTP()
smtp.connect( smtpserver )
smtp.login( username, password )
smtp.sendmail( sender, receiver, msg.as_string() )
smtp.quit()
'''
