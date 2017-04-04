# --*-- coding: utf-8 --*--

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import time
from bs4 import BeautifulSoup
from mysql_io import save_db
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


def crawler():
    try:
        display = Display(visible=0, size=(800, 800))
        display.start()
        driver = webdriver.Chrome()

        login_url = 'https://maimai.cn/login'

        for i in range(1, 20):
            print '尝试第 %s 次登录...' % i
            driver.get(login_url)
            account = driver.find_element_by_name("m")
            password = driver.find_element_by_name("p")
            account.send_keys("你的账号")
            password.send_keys("你的密码")
            submit_btn = driver.find_element_by_xpath("//input[@type='submit']")
            submit_btn.send_keys(Keys.RETURN)
            driver.implicitly_wait(30)
            time.sleep(5)

            if driver.current_url == 'https://maimai.cn/feed_list':
                print '登录成功！'
                break

        page = 0
        STOP_FLAG = False
        while True:
            url = 'https://maimai.cn/sdk/web/gossip_list?u=35592654&channel=www&version=4.0.0&' \
                  '_csrf=zJe5CJyS-YPPqHC8tETpP2jEQwj_LU5WqBBg&' \
                  'access_token=1.078a176c90d7dded811bcfd0534cbd7a&' \
                  'uid=%22lY%2BeNfzJ5sVuqsgvlOW0j%2FAirs3A3wL6ApgZu%2Fo1crA%3D%22&' \
                  'token=%22vWMBa4S7jJrIh%2FgZFmBnAiFMPWWAdl3ZjtMlxgc4XwfWkWV9Ddyn77rGoNNN%2BvfE8CKuzcDfAvoCmBm7%2BjVysA%3D%3D%22&' \
                  'page={page}&jsononly=1'.format(page=page)


            driver.get(url)
            driver.implicitly_wait(30)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            text = soup.text
            json_data = json.loads(text)

            gpssip_list = json_data['data']
            count = json_data['count']
            if count == 0:
                break

            for g in gpssip_list:
                print g['text']
                r = save_db(g)
                if r == 'EXIST':
                    continue

            if STOP_FLAG:
                break
            page += 1

        driver.close()
        display.stop()

    except Exception as e:
        print e
        driver.close()
        display.stop()


if __name__ == '__main__':
    crawler()
