# Created by venka at 5/11/2023
Feature: Verify the item added in amazon cart

  Scenario: User navigates to cart to verify the item added successfully
    Given Open amazon page
    When search the item coffee
    Then Add the coffee link to cart
    Then Click on amazon cart
    Then Verify the coffee is added successfully in cart
