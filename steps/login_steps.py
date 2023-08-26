from behave import *


@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()


@when('I click the cookie button')
def step_impl(context):
    context.login_page.click_accept_cookie()


@when('I insert the email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I insert the password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)


# @when('I click the login button')
# def step_impl(context):
#     context.login_page.click_login()
#
#
# @then('I see no account error displayed')
# def step_impl(context):
#     context.login_page.no_account_error_is_displayed
