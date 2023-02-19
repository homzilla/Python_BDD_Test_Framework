Feature: Login functionality
    As a user
    I want to be able to login to the web application
    So that I can access the protected resources

    Scenario: Successful login
        Given I am on the login page
        When I enter valid credentials
        And I click the login button
        Then I should be redirected to the main page

