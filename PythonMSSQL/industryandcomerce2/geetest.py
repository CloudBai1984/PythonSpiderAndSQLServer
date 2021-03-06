# -*- coding: utf-8 -*-

import time
import uuid
import io

from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains


class BaseGeetestCrack(object):

    """验证码破解基础类"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def input_by_id(self, text=u"中国移动", element_id="keyword_qycx"):
        """输入查询关键词

        :text: Unicode, 要输入的文本
        :element_id: 输入框网页元素id

        """
        input_el = self.driver.find_element_by_id(element_id)
        input_el.clear()
        input_el.send_keys(text)
        time.sleep(3.5)

    def click_by_id(self, element_id="popup-submit"):
        """点击查询按钮

        :element_id: 查询按钮网页元素id

        """
        search_el = self.driver.find_element_by_id(element_id)
        search_el.click()
        time.sleep(3.5)

    def calculate_slider_offset(self):
        """计算滑块偏移位置，必须在点击查询按钮之后调用

        :returns: Number

        """
        img1 = self.crop_captcha_image()
        
        self.drag_and_drop(x_offset=1)
     

        img2 = self.crop_captcha_image()
        w1, h1 = img1.size
        w2, h2 = img2.size
        if w1 != w2 or h1 != h2:
            return False
        left = 0
        flag = False
        for i in range(60, w1):
            for j in range(h1):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    flag = True
                    break
            if flag:
                break
        
        return left -2 

    def is_pixel_equal(self, img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0] < 80) and abs(pix1[1] - pix2[1] < 80) and abs(pix1[2] - pix2[2] < 80)):
            return True
        else:
            return False

    def crop_captcha_image(self, element_id="gt_box"):
        """截取验证码图片

        :element_id: 验证码图片网页元素id
        :returns: StringIO, 图片内容

        """
        global captcha_el
        captcha_el = self.driver.find_element_by_class_name(element_id)
        location = captcha_el.location
        size = captcha_el.size
        browser_x_offset = 0
        browser_y_offset = 0
        #if 'phantomjs' == self.get_browser_name():
        #    browser_x_offset += 171
        #    browser_y_offset += 7
        left = int(location['x'] + browser_x_offset)
        top = int(location['y'] + browser_y_offset)
        right = int(location['x'] + browser_x_offset + size['width'])
        bottom = int(location['y'] + browser_y_offset + size['height'])
        print(left, top, right, bottom)

        screenshot = self.driver.get_screenshot_as_png()

        screenshot = Image.open(io.BytesIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        #captcha.save("%s.png" % uuid.uuid4().hex)

        return captcha

    def get_browser_name(self):
        """获取当前使用浏览器名称
        :returns: TODO

        """
        return str(self.driver).split('.')[2]

    def drag_and_drop(self, x_offset=0, y_offset=0, element_class="gt_slider_knob"):
        """拖拽滑块

        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :element_class: 滑块网页元素CSS类名

        """
        

        dragger = self.driver.find_element_by_class_name(element_class)
     
        action = ActionChains(self.driver)

        action.move_to_element(dragger).perform()
        action.click_and_hold().perform()


        sc = self.driver.get_screenshot_as_png()
        sc = Image.open(io.BytesIO(sc))
        sc.save(r"D:\\test\\_start.png")
        #for i in range(60,x_offset + 20,10):
        #    action.move_to_element_with_offset(captcha_el,i,0).perform()
        #    sc = self.driver.get_screenshot_as_png()
        #    sc = Image.open(io.BytesIO(sc))
        #    sc.save(r"D:\\i.png")
        #for i in range(2):
        #action.move_by_offset(x_offset / 2,0).perform()
        time.sleep(1.5)
       
        action.drag_and_drop_by_offset(dragger, x_offset, y_offset).perform()
        sc = self.driver.get_screenshot_as_png()
        sc = Image.open(io.BytesIO(sc))
        sc.save(r"D:\\test\\_end.png")


        # 这个延时必须有，在滑动后等待回复原状
        time.sleep(4)

    def move_to_element(self, element_class="gt_slider_knob"):
        """鼠标移动到网页元素上

        :element: 目标网页元素

        """
        time.sleep(3)
        element = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(4.5)

    def crack(self):
        """执行破解程序

        """
        raise NotImplementedError
