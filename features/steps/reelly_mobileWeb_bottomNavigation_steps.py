from behave import given, when, then

@when("Click on events button")
def click_events_button(context):
    context.app.mobileWeb_bottomNavigationBar_page.click_events_button()
