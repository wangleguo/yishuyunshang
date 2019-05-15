# -*- coding:utf-8 -*-
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class EmailManager():
    def sendShowAnnex_email(self, msg):
     
        # 邮件对象:
        message = MIMEMultipart()
        message.attach(MIMEText(msg, 'html', 'utf-8'))
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText(msg, 'html', 'utf-8')

        message['from'] = 'service@jishuapp.cn'
        message['to'] = '452768881@qq.com'
        password = "west999@"
        message['subject'] = Header(u'技术小程序个商业解决方案', 'utf-8').encode()
        smtp_server = "smtp.jishuapp.cn"
        server = smtplib.SMTP_SSL('smtp.jishuapp.cn', 465)  # SMTP协议默认端口是25
        # 打印出和SMTP服务器交互的所有信息。
        # server.set_debuglevel(1)
        # 登录SMTP服务器
        server.login(message['from'], password)

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('./images/timg.jpg', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'jpg', filename='timg.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            message.attach(mime)
        # 发邮件，由于可以一次发给多个人，所以传入一个list;
        # 邮件正文是一个str，as_string()把MIMEText对象变成str。
        server.sendmail(message['from'], [message['to']], message.as_string())
        server.quit()
if __name__ == '__main__':
    em = EmailManager()
    em.sendShowAnnex_email('''<html lang="en">
    <body>
    <h1>附件中的图片</h1>
    <img src="cid:0">
    </body>
    </html>''')
