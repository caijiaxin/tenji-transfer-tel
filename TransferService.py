from WebDriverFactory import WebDriverFactory
from Actions import Actions
from MailProvider import MailProvider


class TransferService:

    __driver_path = ''
    __url = 'https://www.hikari.ntt-east.net/AGT_Main.htm'

    __tel = ''
    __tel_password = ''

    __start_or_stop = True
    __mail_subject = ''
    __mail_text = ''

    __mail_account = ''
    __mail_password = ''

    __mail_list = None

    def __init__(self, driver_path, start_or_stop, mail_account, mail_password):
        self.__driver_path = driver_path

        self.__start_or_stop = start_or_stop
        if self.__start_or_stop:
            self.__mail_subject = '电话转送开始'
            self.__mail_text = '电话转送开始'
        else:
            self.__mail_subject = '电话转送结束'
            self.__mail_text = '电话转送结束'

        self.__mail_account = mail_account
        self.__mail_password = mail_password

    def start(self):
        driver = WebDriverFactory.get_chrome_driver(self.__driver_path)
        executor = Actions(driver)

        driver.get(self.__url)

        # 进入登入界面
        executor.click_element('input[title="ログイン"]')

        # 输入账号密码 登入
        executor.input_text('input[id="tel"]', self.__tel)
        executor.input_text('input[id="pass"]', self.__tel_password)
        executor.click_element('input[alt="ログイン"]')

        # 点击ボイスワープ按钮
        executor.click_element('input[alt="ボイスワープ"]')

        # 点击サービス開始／停止按钮
        executor.click_element('input[alt="サービス開始／停止"]')

        # 点击开始单选按钮 设定时间
        if self.__start_or_stop:
            executor.click_element('input[id="r2"]')
            executor.input_text('input[id="call_sec2"]', '5')
        else:
            executor.click_element('input[id="stop"]')
        # 点击设定按钮
        executor.click_element('input[alt="設定"]')

        # 登出
        executor.click_element('input[title="ログアウト"]')

        # 发送邮件
        mail_provider = MailProvider(
            self.__mail_account, self.__mail_password, self.__mail_subject, self.__mail_text)
        mail_provider.send_ｍail(self.__mail_list)

    def set_mail_list(self, mail_list):
        self.__mail_list = mail_list

    def set_tel_and_password(self, tel, password):
        self.__tel = tel
        self.__tel_password = password
