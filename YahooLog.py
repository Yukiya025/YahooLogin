# coding: UTF-8
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # URL関連
    url = "https://login.yahoo.co.jp/config/login"
    login = "Login ID"
    password = "Password"

    # ヘッドレスモードの設定。
    # True => ブラウザを描写しない。
    # False => ブラウザを描写する。
    options = Options()
    options.set_headless(False)

    # Chromeを起動
    driver = webdriver.Chrome(executable_path="/home/ayumka/chromedriver", chrome_options=options)

    # ログインページを開く
    driver.get(url)

    # ログオン処理
    # ユーザー名入力
    driver.find_element_by_id("username").send_keys(login)
    driver.find_element_by_id('btnNext').send_keys(Keys.ENTER)

    # ブラウザの描写が完了させるためにsleep
    sleep(10)

    # パスワード入力
    driver.find_element_by_id("passwd").send_keys(password)
    driver.find_element_by_id("btnSubmit").send_keys(Keys.ENTER)

    # soupオブジェクトを作成
    soup = BeautifulSoup(driver.page_source, "lxml")

    # ログイン後のトップページのソースを表示
    # print(soup)

    # ドライバーをクローズ
    # driver.close()

    driver.get('https://travel.yahoo.co.jp/?sc_e=ytmh')
    print("ログイン成功")