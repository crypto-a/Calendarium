import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_confirmation_email(email_to):
    #TODO: What email is this being sent from?
    email_sender = 'your_email@gmail.com'  # Replace with your email address
    email_password = 'your_password'  # Replace with your email password
    email_subject = 'Welcome to Calendarium!'
    #TODO: Change the email body
    email_body = 'This is a confirmation email.'

    message = MIMEMultipart()
    message['From'] = email_sender
    message['To'] = email_to
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_to, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


