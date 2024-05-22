from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("input {search_query} into target search field")
def input_keyword_into_target_search_field(context, search_query):
    context.driver.find_element(By.ID, 'search').send_keys(search_query)


@when("Click on Target search icon")
def click_on_target_search_icon(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@then("Product results for {keyword} are shown on target page")
def product_results_for_keyword(context, keyword):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print(actual_text)
    assert keyword in actual_text, f'Error! Text {keyword} not in {actual_text}'

