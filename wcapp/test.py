from flask import Flask
from flask.ext.mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'terpiljenya',
    MAIL_PASSWORD = 'cjhjrldf42'
    )

mail=Mail(app)

@app.route("/")
def index():
    msg = Message(
              'Happy Birthday',
           sender='cloud@whatcomputer.com',
           recipients=
               ['amo4ka@ukr.net'])
    msg.body = u"Great cloud wishes you a happy birthday!))"
    mail.send(msg)
    return "Sent"

if __name__ == "__main__":
    app.run()