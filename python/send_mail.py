# Import smtplib for the actual sending function
import os
import smtplib

# Import the email modules we'll need

from email.mime.text import MIMEText


def send_mail(GFROM, GTO, GUSER, GPASS):
    # define variables

    textfile = 'email_message.txt'
    smtp_server = 'smtp.gmail.com'

    # Open a plain text file for reading.  For this example, assume that

    # the text file contains only ASCII characters.

    fp = open(textfile, 'rb')
    # Create a text/plain message

    msg = MIMEText(fp.read())
    fp.close()

    # me == the sender's email address

    # you == the recipient's email address

    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = GFROM
    msg['To'] = GTO

    # Send the message via our own SMTP server, but don't include the

    # envelope header.

    s = smtplib.SMTP(smtp_server, 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(GUSER, GPASS)
    s.sendmail(me, [you], msg.as_string())
    s.quit()


if __name__ == '__main__':
    me = 'imrod.rod@gmail.com'
    you = 'rod.lai@latticeworkinc.com'
    # remember to set ID/PASS in the system
    strGmailUser = os.environ['GmailUser']
    strGmailPassword = os.environ['GmailPASS']
    send_mail(me, you, strGmailUser, strGmailPassword)

