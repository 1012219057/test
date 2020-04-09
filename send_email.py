import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题

"""fffdgdgdg"""
def send_email(spider_name):
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户名密码
    user = 'gql1012219057@163.com'
    password = 'ai712522'

    # 发送和接收邮箱
    sender = 'gql1012219057@163.com'
    receive = 'gql1012219057@163.com'

    # 发送邮件主题和内容
    subject = f'爬虫> {spider_name} <已完成抓取'
    content = f'<html><h1 style="color:red">爬虫> {spider_name} <已完成抓取!</h1></html>'

    # HTML邮件正文
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receive

    # 创建邮件发送类
    smtp = smtplib.SMTP(smtpserver, 25)

    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("开始发送邮件...")
    smtp.sendmail(sender, receive, msg.as_string())
    smtp.quit()
    print("邮件发送完成！")


if __name__ == '__main__':
    send_email('test')
