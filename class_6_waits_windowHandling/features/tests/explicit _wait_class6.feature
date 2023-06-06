Feature: Amazon Signin Test

  Scenario: Amazon user sees Sign in button and disappeared
    Given Open Amazon main page
    When Verify signin is Clickable
    Then wait for 5 seconds
    When Verify signin is Clickable
    Then verify sign-in disappears