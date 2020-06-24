#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 10:33
# @Author  : YaoJa
# 浏览器基本操作
# 引入webdriver
from selenium import webdriver
from time import sleep
# from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    # 初始化浏览器
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    # options = Options()
    # options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\Application\\chrome.exe"
    # driver = webdriver.Chrome(chrome_options=options, executable_path="E:/software/selenium_drivers/chromedriver")

    sleep(1)
    # 浏览器大小设置
    driver.set_window_size(800, 600)
    # 打开某一个url
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.get("https://cn.bing.com/")
    sleep(2)
    # 浏览器最大最小化
    # driver.minimize_window()
    # sleep(2)
    driver.maximize_window()
    sleep(2)
    # 浏览器基本信息获取
    # 当前页面标题，当前url，页面源码/断言类，处理一些特殊情况
    print(driver.title)
    print(driver.current_url)
    # print(driver.page_source)
    # 浏览器导航
    driver.back()
    sleep(2)
    driver.forward()
    sleep(2)
    driver.refresh()
    sleep(2)
    # 关闭当前页面
    # driver.close()
    # 关闭webdriver打开的所有浏览器页面
    driver.quit()
