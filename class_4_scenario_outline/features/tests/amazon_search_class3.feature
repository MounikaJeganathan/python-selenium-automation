# Created by venka at 5/11/2023
Feature: Amazon search test

  Scenario Outline: User can search on amazon
    Given Open Amazon main page
    When Search for <search_term>
    Then verify search result shown for <search_result>
    Examples:
      |search_term| search_result |
      |table      |"table"        |
      |coffee     |"coffee"       |
