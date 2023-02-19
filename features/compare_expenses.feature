Feature: Compare Expenses functionality

  Scenario: User can compare expenses for different periods of time
    Given I am on the login page
    When I enter valid credentials
    And I am on the expenses page
    And I click the "Compare Expenses" button
    And I select the "2019" and "2020" options
    And I click the "Show data" button
    Then I should see a chart comparing the expenses for the selected years
