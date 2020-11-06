import shelve
import time

import exrex as exrex
import rstr as rstr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

class TestWXAddContacts:
    def setup(self):
        #用Chrome的debug形式启动复用浏览器功能，同时要在命令行执行chrome --remote-debugging-port=9222启动一个浏览器
        # option=Options()
        # option.debugger_address="localhost:9222"
        # self.driver=webdriver.Chrome(options=option)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    '''
    测试获取到cookies
    '''
    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # element=self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts > span")
        # 用driver.cookies()可以获取当前页面的cookies。cookies是一个列表，列表中含有多个字典
        # print(self.driver.get_cookies())
        # 把刚刚获取的cookies放入变量中
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851979715689'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Mxle7zup1jX6GmaaLqiCSZ3PCvrglz7ytf9Sg7FdYwmP0qloh6Nu0xhzVf6OtvqsGZYulbZIMjjd6aLgMzELJC4uieJ0iBniaxO-nM-ZOYsLxatYscRpCdPWGyix9T4uTfG6pVhLUaSQccN08ivv1JMl3utsQsrItQ2Ge0cPlG_NTsFz6UIL3Iz7_eZV_DYFExAl9L43K4e4bAG35Jpzg17QuAiZNJqXtF8jOa79wumcqkz8axXpJ5nC8JpocDBDhvV81CpvFL7YTZNG1bQhuw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851979715689'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325118180641'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'rdX8xciG8uPr1TykJDR04UwYNFS_6mlyPo6heqwV8mvUoil4OigSJGgvdzQp-gt6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5119008'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604660133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '25786684683328881'},
            {'domain': '.qq.com', 'expiry': 1667732855, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.64081738.1604659025'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636195021, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1630206036, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/',
             'secure': False, 'value': '519826121442879940'},
            {'domain': '.qq.com', 'expiry': 1630206036, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
             'secure': False, 'value': '1598670036'},
            {'domain': '.qq.com', 'expiry': 1604747255, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.955040286.1604659025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604690557, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8p4mghk'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '8046161920'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'b32dbe42970b49f97b412ef01512e0993d14c33388d9b08726531f8e8e65f5b0'},
            {'domain': '.qq.com', 'expiry': 2147483836, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'AcDZwy1Gai'},
            {'domain': '.qq.com', 'expiry': 1624581815, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'e1n5w993f0q4f5H8z1G5A5w182'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607253040, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'cht'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636196132, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604659023,1604660133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4663551810'}]
        # time.sleep(3)
        # 可以用for循环遍历出每个字典值，然后添加到页面上（添加后就不用再使用debug模式了）
        for cookie in cookies:
            # 有时expiry字段有小数点，而且这个字段在服务器有保存，所以删掉也无所谓
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 有了cookies之后就可以不用扫码登录了，直接刷新一下，就可以进入已登录的主页面
        # self.driver.refresh()
        # time.sleep(3)
    '''
    测试用shelve模块，将保存的cookies，保存到文件中去
    '''
    def test_shelve_demo(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851979715689'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Mxle7zup1jX6GmaaLqiCSZ3PCvrglz7ytf9Sg7FdYwmP0qloh6Nu0xhzVf6OtvqsGZYulbZIMjjd6aLgMzELJC4uieJ0iBniaxO-nM-ZOYsLxatYscRpCdPWGyix9T4uTfG6pVhLUaSQccN08ivv1JMl3utsQsrItQ2Ge0cPlG_NTsFz6UIL3Iz7_eZV_DYFExAl9L43K4e4bAG35Jpzg17QuAiZNJqXtF8jOa79wumcqkz8axXpJ5nC8JpocDBDhvV81CpvFL7YTZNG1bQhuw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851979715689'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325118180641'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'rdX8xciG8uPr1TykJDR04UwYNFS_6mlyPo6heqwV8mvUoil4OigSJGgvdzQp-gt6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5119008'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604660133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '25786684683328881'},
            {'domain': '.qq.com', 'expiry': 1667732855, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.64081738.1604659025'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636195021, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1630206036, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/',
             'secure': False, 'value': '519826121442879940'},
            {'domain': '.qq.com', 'expiry': 1630206036, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
             'secure': False, 'value': '1598670036'},
            {'domain': '.qq.com', 'expiry': 1604747255, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.955040286.1604659025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604690557, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8p4mghk'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '8046161920'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'b32dbe42970b49f97b412ef01512e0993d14c33388d9b08726531f8e8e65f5b0'},
            {'domain': '.qq.com', 'expiry': 2147483836, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'AcDZwy1Gai'},
            {'domain': '.qq.com', 'expiry': 1624581815, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'e1n5w993f0q4f5H8z1G5A5w182'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607253040, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'cht'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636196132, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604659023,1604660133'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4663551810'}]
        # 引入python自带的shelve模块，将cookies的值保存在其中。保存完记得close掉使用
        db=shelve.open("cookies")
        db['cookie']=cookies
        db.close()
    '''
    将生成到文件中的cookies拿出来使用，然后模拟客户操作，实现添加成员
    '''
    def test_add_contacts(self):
        #用上面的方法生成shelve文件，就可以直接引用了
        db=shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        #开始正常访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        element.click()
        time.sleep(2)
        #利用rstr生成随机字符串
        username=rstr.rstr('abcdefghijklmn')
        memberAdd_acctid=rstr.rstr('1234567890',1,10)
        #用exrex类和正则表达式生成手机号
        memberAdd_phone=exrex.getone(r'(13[0-9]|14[5|7]|15[4]|18[0-9]|17[5-8])(\d{8})')
        #模拟用户操作添加成员
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys(memberAdd_acctid)
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_phone').send_keys(memberAdd_phone)
        self.driver.find_element(By.CSS_SELECTOR,'.js_member_editor_form>div:nth-child(3)>a:nth-child(2)').click()
        #如果保存成功该元素的文本信息是“保存成功”
        text=self.driver.find_element(By.CSS_SELECTOR, '#js_tips').text
        assert text == "保存成功"


