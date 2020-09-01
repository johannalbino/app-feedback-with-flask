import smtplib, ssl
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 465
    smtp_server = 'smtp.gmail.com'
    login = 'johann.testes@gmail.com'
    context = ssl.create_default_context()
    password = 'jhja1706'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li>" \
              f"<li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'testes@gmail.com'
    receiver_email = 'johann.testes@gmail.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
