from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search(query):
    url = 'https://www.google.com/'
    search_element = 'q'
    res_xpath = '//*[@id="rso"]/div[2]/div/div/div[1]/a'

    browser = webdriver.Chrome()
    browser.get(url)

    search_input = browser.find_element_by_name(search_element)
    search_input.send_keys(query + Keys.RETURN)

    search_result = browser.find_element_by_xpath(res_xpath)
    print(search_result.get_attribute("href"))
    
    browser.close()

query = input('qual a sua pesquisa?: ')
search(query)

