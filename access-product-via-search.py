from selenium import webdriver
from behave import given,when,then

driver= webdriver.Chrome()
driver.get("https://ebay.com")
print(driver.title)

class Search():
    def __init__(self, category1,category2):
        # Search the Product via search box
        print('CURRENT:', category1)
        category_search_box = driver.find_element("xpath", '/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]')
        category_search_box.click()
        category_search_box.send_keys(category1)
        clear_the_search_box = driver.find_element('xpath', "/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
        clear_the_search_box.clear()
        category_search_box = driver.find_element("xpath", '/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]')
        category_search_box.send_keys(category2)
        click_search_button = driver.find_element('xpath',"/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input")
        click_search_button.click()
        print(driver.title)
        # back_to_screen = driver.find_element('xpath', "//a[@id='gh-la']")
        # back_to_screen.click()
        driver.implicitly_wait(0.5)

p1 = Search("Macbook","Computers/Tablets & Networking")

