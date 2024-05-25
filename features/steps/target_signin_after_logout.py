from behave import given, when, then


@when('click sign in')
def click_sign_in(context):
    context.app.login_page.click_sign_in()


@when('click Sign In after it opens right side navigation menu')
def click_sign_in_again(context):
    context.app.login_page.click_sign_in_again()


@then('sign In form opens')
def verify_sign_in_form(context):
    signin_form_heading_txt = context.app.login_page.verify_sign_in_form()
    assert signin_form_heading_txt is not None



