# Created by venka at 6/2/2023
Feature: Test for 404 page

 Scenario: User is able to navigate amazon blog
    Given Amazon product B081YS2F7N1111 page
    And Store Original window
    When Click on dog image
    And Switch to new window
    Then Verify blog is opened
    And close blog
    And Return to orginial window

