# Created by venka at 5/11/2023
Feature: Amazon UI page

  Scenario: User can see language options
    Given Open Amazon main page
    When Hover over the language option
    Then Verify Spanish option present



  Scenario: Verify that user can search in department
    Given Open Amazon main page
    When Select department books
    And Search for Faust
    Then Verify correct department shown as book

