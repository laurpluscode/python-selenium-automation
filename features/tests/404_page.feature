# Created by Lauren at 12/27/21
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon blog from 404 error
    Given Open Amazon page
    And Store original window
    When Click on dog image
    And Switch to new window
    Then Verify blog is opened
    And Close Blog
    And Return to original window