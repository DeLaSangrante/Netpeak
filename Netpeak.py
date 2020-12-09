from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import unittest

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://netpeak.ua/")

career = driver.find_element_by_link_text("Карьера").click()
workInNetpeak = driver.find_element_by_link_text("Я хочу работать в Netpeak").click()
upFile = driver.find_element_by_id("upload").click()

time.sleep(2) 
pyautogui.write(r"1submission")
time.sleep(2)
pyautogui.press('enter')


errorText = driver.find_element_by_id("up_file_name")
time.sleep(2)
assert errorText.text == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

name = driver.find_element_by_id("inputName").send_keys('Mykola')
lastName = driver.find_element_by_id("inputLastname").send_keys('Mykola')
inputEmail = driver.find_element_by_id("inputEmail").send_keys('Mykola@ukr.net')
year = driver.find_element_by_name("by").send_keys('1997')
month = driver.find_element_by_name("bm").send_keys('августа') 
day = driver.find_element_by_name("bd").send_keys('1')
phone = driver.find_element_by_id("inputPhone").send_keys('+380972704145')

time.sleep(1)

submitBttn = driver.find_element_by_id("submit").click()

time.sleep(1)
warning = driver.find_element_by_css_selector("body > div:nth-child(4) > div > p")
assert warning.text == "Все поля являются обязательными для заполнения"

time.sleep(1)


curses = driver.find_element_by_link_text("Курсы").click()
time.sleep(2)
assert driver.title == 'Образовательный Центр Netpeak: курсы по SEO, PPC, PHP в Одессе'

time.sleep(1)

driver.quit()








