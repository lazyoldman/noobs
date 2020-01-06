from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class AutoTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.fstcode.com/")
        self.driver.maximize_window()
        self.time = time.sleep(3)

    def login(self):
        self.driver.find_element_by_id("ls_username").send_keys("lazzyang")
        self.driver.find_element_by_id("ls_password").send_keys("1994623240")
        self.driver.find_element_by_xpath(r"//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button/em").click()
        time.sleep(5)
        get_login = self.driver.find_element_by_xpath("//*[@id='um']/p[1]/a[5]").text
        if get_login == "退出":
            print('登录成功')
        else:
            print("登录失败")

if __name__ == '__main__':
    test = AutoTest()
    test.login()

