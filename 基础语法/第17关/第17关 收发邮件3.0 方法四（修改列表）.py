
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv
from_addr = '76746694@qq.com'
password = 'fkbefpkgscnxcbcj'

data = [['76746694@qq.com'],['whzjz_1982@163.com']]
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row
        print(to_addrs)
        smtp_server = 'smtp.qq.com'
        test='''静夜思
        李白
        床前明月光，
        疑是地上霜
        举头望明月，
        低头思故乡。'''
        msg = MIMEText(test,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(str(to_addrs))
        msg['Subject'] = Header('静夜思方法四')
        # server = smtplib.SMTP_SSL(smtp_server)
        # server.connect(smtp_server,465)
        server = smtplib.SMTP()
        server.connect(smtp_server,25)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()

