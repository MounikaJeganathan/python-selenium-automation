# Created by venka at 5/11/2023
Feature: Amazon search test

  Scenario: User can search for table in amazon
    Given Open Amazon main page
    When Search for table
    Then verify search result shown for "table"

 Scenario: User can search for coffee in amazon
    Given Open Amazon main page
    When Search for coffee
    Then verify search result shown for "coffee"