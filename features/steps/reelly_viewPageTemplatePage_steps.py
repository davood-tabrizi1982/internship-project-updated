from behave import given, when, then

@then('Verify the button “Send my CV” button is available.')

def verify_send_my_cv_available(context):
    context.app.viewPageTemplate_page.verify_send_my_cv_text()