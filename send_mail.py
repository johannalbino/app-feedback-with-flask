import smtplib
import ssl
import os
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    if os.environ.get('DEBUG'):
        env = os.environ.get
    else:
        from environs import Env
        env = Env()
        env.read_env()
    port = env('PORT_EMAIL')
    smtp_server = env('SMTP_EMAIL')
    login = env('LOGIN_EMAIL')
    context = ssl.create_default_context()
    password = env('PASSWORD_EMAIL')
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li>" \
              f"<li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'example@example.com'
    receiver_email = env('LOGIN_EMAIL')

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
