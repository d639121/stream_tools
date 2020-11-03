#!/usr/bin/python
# @Time  : 2020/3/25 16:01
# @Author: LOUIE
# @Desc  : 邮件发送

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config_log import log
from smtplib import SMTP, SMTP_SSL, SMTPException
from utils import wechat_hook
from email.header import Header


class ConfigEmail:

    on_off = 'on'

    def __init__(self):
        self.username = 'autotest_sender@tanzhou.cn'
        self.recievers = ['helvyi@tanzhou.cn']
        self.email_host = 'smtp.mxhichina.com'
        self.email_port = 465
        self.password = 'TZ#Eb2xpn'
        self.subject = 'apiFlowAutoTest'
        self.content = wechat_hook.struct_desc()
        self.msg = MIMEMultipart()
        self.msg["To"] = ",".join(self.recievers)
        print(self.msg["To"])
        self.msg["From"] = Header(self.username, 'utf-8')
        self.msg["Subject"] = Header(self.subject, 'utf-8')
        self.smtp = SMTP()


    def email_content(self):
        content = MIMEText(self.content, _subtype='plain', _charset="utf-8")
        self.msg.attach(content)

    def send_email(self):
        self.email_content()

        try:
            self.smtp.connect(self.email_host)
            self.smtp = SMTP_SSL(self.email_host, timeout=5)
            # self.smtp.ehlo_or_helo_if_needed()
            self.smtp.login(self.username, self.password)
            self.smtp.sendmail(self.username, self.recievers, self.msg.as_string().encode())
            log.info("##### 邮件发送成功 ！！！！！")
        except SMTPException as e:
            log.error("////// 发送邮件失败，错误：%s" %e)
        finally:
            self.smtp.close()
            self.smtp.quit()


if __name__ == '__main__':
    ce = ConfigEmail()
    ce.send_email()