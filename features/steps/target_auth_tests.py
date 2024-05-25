from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.driver.get("https://www.target.com/account")


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.login_page.click_on_target_tac_link()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.target_app_page.verify_tac_page_opened()


@then('User can close new window and switch back to original')
def switch_to_original(context):
    context.app.target_app_page.switch_window_by_id(context.original_window)



