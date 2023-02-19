Feature: Chart Display

  Scenario: View data in a chart format
    Given the user is logged in
    When the user clicks on the "Compare Expenses" button
    And the user clicks on the "Show data for next year" button
    And the user clicks on the "Compare Expenses" button
    And the user clicks on the "Show data for next year" button
    And the user clicks on the "Show expenses chart" button
    Then the expenses chart should be displayed
