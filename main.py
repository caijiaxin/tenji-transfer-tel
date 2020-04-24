from TransferService import TransferService
import time

now = time.strftime('%H', time.localtime(time.time()))
if now == 10:
    is_start = True
else:
    is_start = False

# 写上你的谷歌驱动地址
driver_path = ''

# 写上你的Gmail邮箱
mail_account = ''

# 写上你的Gmail邮箱的app密码
mail_password = ''

# 写上你要通知的上司的邮箱
mail_list = ['', '', '', '']

service = TransferService(driver_path, is_start, mail_account, mail_password)
service.set_mail_list(mail_list)
service.start()
