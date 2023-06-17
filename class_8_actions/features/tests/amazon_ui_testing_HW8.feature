# Created by venka at 6/16/2023
Feature:Amazon UI testing


  Scenario: Verify that user can search in department
    Given Open Amazon main page
    When Select department baby
    And Search for bottle
    Then Verify correct department shown as baby


  Scenario: Verify that user can see deals on hovering on product
    Given Open Amazon product B074TBCSC8 page
    When Hover on New Arrivals
    Then Verify deals are displaying