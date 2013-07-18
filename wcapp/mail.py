from flask.ext.mail import Message
from wcconfig import app, ADMINS, mail
from decorators import async


# @async
def send_async_email(msg):
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body=""):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def save_feedback(message, email):
    send_email(email, email, ADMINS, message)


def send_admin_messages(subject, sender, text):
    msg = Message(subject, recipients=ADMINS)
    msg.body = "From: {0}\nText: {1}".format(sender, text)
    send_async_email(msg)
    return 'ololo'
