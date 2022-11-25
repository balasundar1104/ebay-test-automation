import time
from selenium import webdriver


#launch the google Chrome Browser
driver = webdriver.Chrome()

#Go to ebay.com website
driver.get("https://www.ebay.com/")
title = driver.title
print(title)
driver.maximize_window()

#search the category as electronics
category_search_box = driver.find_element('xpath', "/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
category_search_box.click()
category_search_box.send_keys("Electronics")
click_search_button= driver.find_element('xpath', "/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input")
click_search_button.click()

#clear the Electronics text from search bar
clear_the_search_box= driver.find_element('xpath', "/html/body/div[3]/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
clear_the_search_box.clear()

#Enter the new category name after clearing the old search category
search_new_category = driver.find_element('xpath', "/html/body/div[3]/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
search_new_category.click()
search_new_category.send_keys("Cell Phones & accessories")

#Search the new category as Cellphones & Accessories
click_search_for_new_category= driver.find_element('xpath', "/html/body/div[3]/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input")
click_search_for_new_category.click()
driver.implicitly_wait(5)

#Select cell phones and smart phones option on the left side navigation panel
select_category= driver.find_element('xpath',"/html/body/div[8]/div[3]/ul/li[1]/ul/li[1]/div[2]/ul/li/ul/li[1]/ul/li[2]/a")
select_category.click()

#Select see all button under the brand filter
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
click_see_all_under_brand= driver.find_element('xpath', "/html/body/div[8]/div[3]/ul/li[1]/ul/li[2]/ul/li[1]/div[2]/div/span/button")
click_see_all_under_brand.click()
time.sleep(5)


#Select the filters based on the requirement
class Filters():
    def __init__(self, filter_xpath, check_box_xpath):
        filter_for_selection= driver.find_element("xpath", filter_xpath)
        filter_for_selection.click()
        filter_for_checkbox= driver.find_element("xpath", check_box_xpath)
        filter_for_checkbox.click()
        time.sleep(5)

screen_size_filter = Filters('/html/body/div[18]/div[2]/div/form/div[1]/div[1]/div/div[8]','/html/body/div[18]/div[2]/div/form/div[1]/div[2]/div[1]/div/fieldset/div[1]/div[2]/label/div/span/input')
price_selection_filter= Filters('/html/body/div[18]/div[2]/div/form/div[1]/div[1]/div/div[23]','/html/body/div[18]/div[2]/div/form/div[1]/div[2]/div[1]/div/fieldset/ul/li[2]/div/label/div/span/input')
item_location_filter= Filters('/html/body/div[18]/div[2]/div/form/div[1]/div[1]/div/div[25]','/html/body/div[18]/div[2]/div/form/div[1]/div[2]/div[1]/div/fieldset/div[3]/div/span/input')

#Click apply when after applying all the filters
apply_all_filters = driver.find_element('xpath', "/html/body/div[18]/div[2]/div/form/div[3]/div[2]/button")
apply_all_filters.click()
driver.implicitly_wait(20)
driver.close()