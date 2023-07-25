import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@given('launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when('open flipkart website')
def step_impl(context):
    context.driver.get("https://www.flipkart.com/")
    try:
        context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
    except:
        pass


@then('search for dell laptop')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys("Dell laptop")
    context.driver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(Keys.ENTER)


@then('search for "{searchkeyword}"')
def step_impl(context, searchkeyword):
    context.driver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(searchkeyword)
    context.driver.find_element(By.CSS_SELECTOR, "[type='text']").send_keys(Keys.ENTER)


@then('verify search results based on "{searchkeyword}"')
def step_impl(context, searchkeyword):
    search_result = context.driver.find_element(By.CSS_SELECTOR, "span[class] span").text
    if searchkeyword in search_result:
        print("Search result is based on the keyword searched")
    else:
        print("Search result is not based on the keyword searched")


@then('select checkbox filter')
def step_impl(context):
    # explicit wait is used here
    time.sleep(3)
    WebDriverWait(context.driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "section [title] [type='checkbox']")))
    context.driver.find_element(By.CSS_SELECTOR, "section [title] label div").click()
    time.sleep(3)


@then('select Dell laptop')
def step_impl(context):
    global product_title
    time.sleep(3)
    product_title = context.driver.find_element(By.CSS_SELECTOR, "[class*='row'] div  div").text
    print(product_title)
    context.driver.find_element(By.CSS_SELECTOR, "[class*='row'] div  div").click()
    time.sleep(3)


@then('In Dell product detail page get the product title')
def step_impl(context):
    product_detailpage_title = context.driver.title
    print(product_detailpage_title)


@then('close the browser')
def step_impl(context):
    context.driver.quit()
