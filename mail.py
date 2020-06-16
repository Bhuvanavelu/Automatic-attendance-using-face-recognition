import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
#enter your mail id here#   
fromaddr = "bhuvanavelu2599@gmail.com"
#enter the respective person's mail id#
toaddr = "jayanthivelu2108@gmail.com"
msg = MIMEMultipart()    
msg['From'] = fromaddr   
msg['To'] = toaddr 
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
#set the xl sheet path here#
filename = r'C:\Users\Bhuvanavelu\Downloads\Face-recognition-attendance-system-master\Face-recognition-attendance-system-master\new_writting.xls'
attachment = open(r"C:\Users\Bhuvanavelu\Downloads\Face-recognition-attendance-system-master\Face-recognition-attendance-system-master\\new_writting.xls", "rb") 
part = MIMEBase('application', 'octet-stream') 
part.set_payload((attachment).read())  
encoders.encode_base64(part)    
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
msg.attach(part) 
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls()
#enter your mail id's password#
server.login(fromaddr, "apoo01aishu22") 
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text) 
server.quit() 
