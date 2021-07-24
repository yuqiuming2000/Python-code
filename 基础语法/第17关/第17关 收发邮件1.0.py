import smtplib
from email.mime.text import MIMEText
from_addr = '76746694@qq.com'
password = 'fkbefpkgscnxcbcj'
to_addr = '76746694@qq.com'
smtp_server = 'smtp.qq.com'
msg = MIMEText('HELLO WORD','plain','utf-8')
# server = smtplib.SMTP_SSL(smtp_server)
# server.connect(smtp_server,465)
server = smtplib.SMTP()
server.connect(smtp_server,25)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()


