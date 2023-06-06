# Created by venka at 6/2/2023
Feature: Switching the windows

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    And Store Original window
    When Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original