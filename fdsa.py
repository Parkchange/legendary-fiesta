from selenium import webdriver
import time
br=webdriver.Chrome("c:\python\chromedriver")
br.get("http://naver.com")

aa="dbwlstnwls0"
bb="recruit0504!"
br.find_element_by_css_selector("#id").send_keys(aa)
br.find_element_by_css_selector("#pw").send_keys(bb)

time.sleep(2)

br.find_element_by_css_selector('#frmNIDLogin > fieldset > span > input[type="submit"]').click()
time.sleep(3)
br.find_element_by_css_selector('#PM_ID_ct > div.header > div.section_navbar > div.area_navigation > ul:nth-child(1) > li:nth-child(1) > a > span.an_icon').click()

time.sleep(5)
br.quit()