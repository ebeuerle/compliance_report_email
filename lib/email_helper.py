import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
class EmailHelper(object): 
    def __init__(self):
        self.msg = MIMEMultipart()
        self.from_address = "user@example.com"
	self.email_srv = "smtp.gmail.com"
	self.email_srv_port = "587"
	self.username = "user@example.com"
	self.password = "XXXXXX"
        self.body = "TEXT YOU WANT TO SEND"
 
    def send_email(self,to_address,subject,filename_with_path):
	self.msg['From'] = self.from_address
	self.msg['To'] = to_address
	self.msg['Subject'] = subject 
 
 
	self.msg.attach(MIMEText(self.body, 'plain'))
 
	filename = os.path.basename(filename_with_path)
	attachment = open(filename_with_path, "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	self.msg.attach(part)
 
	server = smtplib.SMTP(self.email_srv, self.email_srv_port)
	server.starttls()
	server.login(self.username, self.password)
	text = self.msg.as_string()
	server.sendmail(self.from_address, to_address, text)
	server.quit()
