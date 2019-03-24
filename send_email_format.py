from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_mail(mailAddress, mailPassword, mailto):
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(mailAddress, mailPassword)
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Hello There!"
        msg["From"] = mailAddress
        msg["To"] = mailto
        html_text = """
        <html>
            <head></head>
            <body>
                <p>Hey!</br>
                    Testing <b>this email</b> <a href="facebook.com">Try this link !</a>
                </p>
            </body>
        </html>
        """
        msg.attach(MIMEText(html_text, "html"))
        mailServer.sendmail(mailAddress, mailto, msg.as_string())
        print("Mail has been sent.")
        mailServer.quit()
    except smtplib.SMTPResponseException:
        print("Mail failed to send.")
        mailServer.quit()

mailAddress = "youremailaddresshere"
mailPassword = "yourpasswordhere"
mailto = "yourtargethere"

send_mail(mailAddress, mailPassword, mailto)