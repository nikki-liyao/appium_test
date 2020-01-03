import time
from appium import webdriver
desired_caps=dict()
desired_caps['platformName']='Android'
desired_caps['platformVersion']='9.0'
desired_caps['deviceName']='Google'
desired_caps['appPackage']='video.downloader.videodownloader'
desired_caps['appActivity']='video.downloader.videodownloader.activity.MainTabsActivity'
driver =webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(10)
driver.quit()
