# Created by venka at 5/29/2023
Feature: Amazon products have image and name

  Scenario: User checks all amazon products have image and name
    Given Open Amazon main page
    When  search the item coffee
    Then Verify result have images and name for all products