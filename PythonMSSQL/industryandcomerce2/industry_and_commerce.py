#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import time
import threading
from geetest import BaseGeetestCrack
from selenium import webdriver
from PIL import Image


class IndustryAndCommerceGeetestCrack(BaseGeetestCrack):

    """工商滑动验证码破解类"""

    def __init__(self, driver):
        super(IndustryAndCommerceGeetestCrack, self).__init__(driver)

    def crack(self):
        """执行破解程序
        """
        self.input_by_id()
        self.click_by_id()
        
        x_offset = self.calculate_slider_offset()
        self.drag_and_drop(x_offset=x_offset)


def run():
    global isRun
    isRun = True
    global driver
    driver = webdriver.PhantomJS()
    driver.get("http://bj.gsxt.gov.cn/sydq/loginSydqAction!sydq.dhtml")
    cracker = IndustryAndCommerceGeetestCrack(driver)
    cracker.crack()
    print(driver.get_window_size())
    time.sleep(3)
    driver.save_screenshot("screen.png")
    driver.close()
    isRun = False

def screenshot():
    time.sleep(5)
    x=0
    while(isRun):
        try:
            sc = driver.get_screenshot_as_png()
            sc = Image.open(io.BytesIO(sc))
            sc.save(r"D:\\test\\" + str(x) + ".png")
            time.sleep(0.1)
            x += 1
        except Exception as e :
            print(str(e))
        pass


def main():
   t1 = threading.Thread(target=run)
   t1.start()
   t2 = threading.Thread(target=screenshot)
   t2.start()
   time.sleep(1000)


if __name__ == "__main__":
    main()
