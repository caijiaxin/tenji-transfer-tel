from email.mime.text import MIMEText
import smtplib


class MailProvider:
    __account = ''
    __password = ''

    __subject = ''
    __message = ''

    def __init__(self, account, password, mail_subject, mail_text):
        self.__account = account
        self.__password = password
        self.__subject = mail_subject
        self.__message = mail_text

    def send_ｍail(self, mail_list):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.__account, self.__password)
        for mail in mail_list:
            message_form = self.__create_message_form(mail)
            server.send_message(message_form)
        server.quit()

    def __create_message_form(self, to_mail):
        message_form = MIMEText(self.__message, "html")
        message_form['Subject'] = self.__subject
        message_form['From'] = self.__account
        message_form['To'] = to_mail
        return message_form

    def set_subject(self, subject):
        self.__subject = subject

    def set_message(self, message):
        self.__message = message
