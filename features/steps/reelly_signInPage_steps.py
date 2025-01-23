from behave import given, when, then

@when("Log in to the page.")

def sign_in(context):
    context.app.signIn_page.signin_username()
    context.app.signIn_page.signin_password()
    context.app.signIn_page.signin_button()