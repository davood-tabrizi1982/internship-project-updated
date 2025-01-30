# Created by Davood at 2025-01-16
Feature: view page template


  Scenario: User can open market tab and go to the view page template
    Given Open the main page https://soft.reelly.io
    When  Log in to the page.
    When  Click on “Market” at the left side menu.
    Then  Verify the right page opens after clicking 'Market' button.
    When  Click on 'Add Company' button.
    Then  Verify the right page opens after clicking 'Add Company' button.
    When  Scroll down and click on the button “View Page Template”
    Then  Verify the button “Send my CV” button is available.




  Scenario: User can open market tab and go to the view page template(mobile web)
    Given Open the main page https://soft.reelly.io
    When  Log in to the page.
    And   Click on events button
    When  Click on “companies” at the top left of the page.
    Then  Verify the right page opens after clicking 'Market' button.
    When  Click on 'Add Company' button.
    Then  Verify the right page opens after clicking 'Add Company' button.
    When  Scroll down and click on the button “View Page Template”
    Then  Verify the button “Send my CV” button is available.
