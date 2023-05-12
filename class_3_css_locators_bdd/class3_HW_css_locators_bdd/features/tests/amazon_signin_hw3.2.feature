# Created by venka at 5/11/2023
Feature: Amazon sign-in page testcase

  Scenario: User should navigate to sign-in page
    Given Open Amazon main page
    When Click on orders
    Then verify sign-in page is opened
