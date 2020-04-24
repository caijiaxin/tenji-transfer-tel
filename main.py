from WebDriverFactory import WebDriverFactory
from Actions import Actions

driver_path = '/Users/shiraishi/Downloads/chromedriver'
driver = WebDriverFactory.getChromeDriver(driver_path)
executor = Actions(driver)

url = 'https://www.hikari.ntt-east.net/AGT_Main.htm'
driver.get(url)

# 进入登入界面
executor.clickElement('input[title="ログイン"]')

# 输入账号密码 登入
executor.inputText('input[id="tel"]', '0364108562')
executor.inputText('input[id="pass"]', 'noah2001')
executor.clickElement('input[alt="ログイン"]')

# 点击ボイスワープ按钮
executor.clickElement('input[alt="ボイスワープ"]')

# 点击サービス開始／停止按钮
executor.clickElement('input[alt="サービス開始／停止"]')

# 点击开始单选按钮 设定时间
executor.clickElement('input[id="r2"]')
executor.inputText('input[id="call_sec2"]', '5')

# 点击设定按钮
executor.clickElement('input[alt="設定"]')

# 登出
executor.clickElement('input[title="ログアウト"]')
