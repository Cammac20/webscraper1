from selenium import webdriver

url = 'https://www.tryhackme.com/'
browser = webdriver.Firefox()
browser.get(url)
browser.maximize_window()