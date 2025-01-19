from behave import given, when, then


@given("Open the main page https://soft.reelly.io")
def open_main(context):
    context.app.main_page.open_main()

