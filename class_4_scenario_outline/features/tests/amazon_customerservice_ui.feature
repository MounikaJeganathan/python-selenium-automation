# Created by venka at 5/18/2023
Feature: Amazon customer Service UI testing

  Scenario: Testing the links in Customer service page
    Given Open Customerservice page
    When Verify welcome note present
    Then Verify 10 UI element
    Then Verify library tab
    Then Verify 11 help topics