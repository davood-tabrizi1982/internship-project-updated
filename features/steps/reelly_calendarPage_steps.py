from behave import given, when, then

@when  ('Click on “companies” at the top left of the page.')
def click_companies_button(context):
    context.app.calendar_page.click_companies_button()