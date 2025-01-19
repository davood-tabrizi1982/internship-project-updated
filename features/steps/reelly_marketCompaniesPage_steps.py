from behave import given, when, then

@then("Verify the right page opens after clicking 'Market' button.")
def verify_market_page(context):
    context.app.marketCompanies_page.verify_market()

@when("Click on 'Add Company' button.")
def click_add_company(context):
    context.app.marketCompanies_page.click_add_company()