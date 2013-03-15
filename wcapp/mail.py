from flask.ext.mail import Message
from wcconfig import app, ADMINS, mail

def save_feedback(message, email):
    msg = Message(email, sender = email, recipients = ADMINS)
    msg.body = message
    mail.send(msg)
