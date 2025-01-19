from behave import given, when, then

@then("Verify the right page opens after clicking 'Add Company' button.")

def verify_presentation_agency(context):
    context.app.presentationAgency_page.verify_presentation_agency_page()

@when('Scroll down and click on the button “View Page Template”')

def click_view_page_button(context):
    context.app.presentationAgency_page.click_view_page_button()