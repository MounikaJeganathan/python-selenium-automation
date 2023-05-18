# Created by venka at 5/18/2023
Feature: Amazon opens bestseller page
  # Enter feature description here

  Scenario: Users see the 5 links in bestseller page
    Given Open Amazon main page
    When Click on Best Seller
    Then Verify the 5 links