from behave import given, when, then

@when('Click on “Market” at the left side menu.')
def click_market(context):
    context.app.sideNavigation_page.click_market()
