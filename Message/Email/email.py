# -*- encoding: utf-8 -*-
'''
@File    :   email.py
@Time    :   2024/12/10 18:52:18
@Author  :   chaopaoo12 
@Version :   1.0
@Contact :   chaopaoo12@hotmail.com
'''

# here put the import lib


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 构建邮件头信息，包括发件人，接收人，标题等
from email.header import Header
from imbox import Imbox


def send_email(mail_title, msg, date, smtpserver, smtpport, msg_from, msg_to, passwd):
    smtpserver = smtpserver
    smtpport = smtpport
    msg_from = msg_from                            #发送方邮箱
    passwd = passwd                                 #填入发送方邮箱的授权码
    msg_to = msg_to                                 #收件人邮箱
    subject = mail_title                           #主题
    if isinstance(msg, str):
        html = msg + ' wrong in {date}'.format(date= date)
    else:
        html = msg
    content_html = MIMEText(html, "html", "utf-8")
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(subject)
    msg["From"] = msg_from
    msg.attach(content_html)
    s = smtplib.SMTP_SSL(smtpserver, smtpport)#邮件服务器及端口号
    try:
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except:
        print("发送失败")
    finally:
        s.quit()


def reademail(mail_title, smtpserver, msg_from, passwd, seen=False):
    with Imbox(smtpserver, msg_from, passwd, ssl=True) as imbox:
        all_inbox_messages = imbox.messages(folder='&UXZO1mWHTvZZOQ-/Report', unread=True)
        for uid, message in all_inbox_messages:
            if message.subject == mail_title:
                htmlbody=message.body['html']
                if seen == True:
                    imbox.mark_seen(uid)
                return(htmlbody)
