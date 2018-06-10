#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import logging
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

logging.basicConfig(level=logging.DEBUG)
debug = logging.debug

__author__ = 'LY'

'''
    
'''


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def mail(imgPath):
    # Email地址和口令:
    from_addr = "2713151713@qq.com"
    password = "zkgiqlibpkrwdhcb"
    # 收件人地址:
    to_addr = '2304709476@qq.com'
    # SMTP服务器地址:
    smtp_server = "smtp.qq.com"

    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Rspi <%s>' % from_addr)
    msg['To'] = _format_addr('LY<%s>' % to_addr)
    msg['Subject'] = Header('Rspi监控邮件', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(imgPath, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpeg', filename='capture.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='capture.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        print("邮件已经发送...")
        server.quit()


def main():
    pass


if __name__ == '__main__':
    main()
