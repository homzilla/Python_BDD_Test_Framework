Feature: Dynamic Content
    As a user
    I want to see dynamic ads on the web page
    So that I can view different ads every time I refresh the page

    Scenario: Dynamic ads are displayed correctly
        Given I am on the expenses page
        When I refresh the page
        Then I should see different dynamic ads on the page
