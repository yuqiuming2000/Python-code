import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '76746694@qq.com'
password = 'fkbefpkgscnxcbcj'
# to_addr = 'whzjz_1982@163.com'
to_addrs = '76746694@qq.com,whzjz_1982@163.com'
smtp_server = 'smtp.qq.com'
test='''静夜思
李白
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
msg = MIMEText(test,'plain','utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('静夜思')
# server = smtplib.SMTP_SSL(smtp_server)
# server.connect(smtp_server,465)
server = smtplib.SMTP()
server.connect(smtp_server,25)
server.login(from_addr, password)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()


