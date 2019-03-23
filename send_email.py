import smtplib

def send_mail(mailAddress, mailPassword, mailto, msg, subject):
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(mailAddress, mailPassword)
        message = "Subject: {}\n\n{}".format(subject, msg)
        mailServer.sendmail(mailAddress, mailto, message)
        print("Mail has been sent.")
        mailServer.quit()
    except:
        print("Mail failed to send.")
        mailServer.quit()

mailAddress = input("What is your gmail address? \n")
mailPassword = input("What is the password for that email address? \n")
mailto = input("What email address do you want to send your message to? \n")
msg = input("What is your message? \n")
subject =  input("What is the subject of the message? \n")

send_mail(mailAddress, mailPassword, mailto, msg, subject)