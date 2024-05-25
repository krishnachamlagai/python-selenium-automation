from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then


SEARCH_ELEMENT = (By.ID, 'search')
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_HEADING_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")


@when("input {search_query} into target search field")
def input_keyword_into_target_search_field(context, search_query):
    context.wait.until(ec.presence_of_element_located(SEARCH_ELEMENT))
    context.app.header.search_product(search_query)


@when("Click on Target search icon")
def click_on_target_search_icon(context):
    context.wait.until(ec.presence_of_element_located(SEARCH_BUTTON))
    context.driver.find_element(SEARCH_BUTTON).click()


@then("Product results for {keyword} are shown on target page")
def product_results_for_keyword(context, keyword):
    context.wait.until(ec.visibility_of_element_located(SEARCH_RESULT_HEADING_TEXT))
    search_result_text = context.driver.find_element(*SEARCH_RESULT_HEADING_TEXT).text
    assert keyword in search_result_text, f'Error! Text {keyword} not in {search_result_text}'

