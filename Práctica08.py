## Incompleto

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from sys import argv 


msg = MIMEMultipart()

message = argv[3]

msg['From'] = argv[1]

msg['Subject'] = argv[2]

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

server.login(argv[1], argv[5])

msg['To'] = argv[4]

server.sendmail(msg['From'], msg['To'], msg.as_string())

print("successfully sent email to:", (msg['To']))

server.quit()



