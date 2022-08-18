from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.tryhackme.com/login')

def thm():
    python_button = browser.find_element_by_xpath('//*[@id="wrapper"]/div[2]/form/div[1]/input')[0]
    python_button.send_keys("macneilcameron1@gmail.com")