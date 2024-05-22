from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CELL_ELEMENTS = (By.XPATH, '//a[@data-test="@web/slingshot-components/CellsComponent/Link"]')


@given('Open Target Circle Page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@when('Get all benefit cells within circle')
def get_all_benefit_cells(context):
    context.driver.find_elements(*CELL_ELEMENTS)
    sleep(2)


# @then('Verify 10 Benefit cells are present')
# def total_10_benefit_cells(context):
#     total_cells = context.driver.find_elements(*CELL_ELEMENTS)
#     count = len(total_cells)
#     assert count == 10, f"Expected 10 benefit, got {len(total_cells)}"


@then('Verify {expected_amount} Benefit cells are present')
def total_10_benefit_cells(context, expected_amount):
    total_cells = context.driver.find_elements(*CELL_ELEMENTS)
    count = len(total_cells)
    assert count == int(expected_amount), f"Expected 10 benefit, got {len(total_cells)}"
