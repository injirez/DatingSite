import smtplib, ssl

def send_email(receiver_email, message):
    port = 465  # For SSL
    smtp_server = 'smtp.gmail.com'
    sender_email = 'emailer.python7@gmail.com' # Enter your address
    password = 'testQwerty1337'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
