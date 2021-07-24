import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '76746694@qq.com'
password = 'fkbefpkgscnxcbcj'
# to_addr = 'whzjz_1982@163.com'
to_addr = '76746694@qq.com'
smtp_server = 'smtp.qq.com'
test='''静夜思
李白
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
msg = MIMEText(test,'plain','utf-8')
msg['From'] = Header('小可爱')
msg['To'] = Header('天气不错')
msg['Subject'] = Header('静夜思')
# server = smtplib.SMTP_SSL(smtp_server)
# server.connect(smtp_server,465)
server = smtplib.SMTP()
server.connect(smtp_server,25)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()


