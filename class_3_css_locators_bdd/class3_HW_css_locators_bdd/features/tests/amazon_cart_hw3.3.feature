# Created by venka at 5/11/2023
Feature: Open Amazon Cart

  Scenario: User navigate to Amazon Cart
    Given Open amazon link
    When Click on Cart icon
    Then Verify amazon cart is empty