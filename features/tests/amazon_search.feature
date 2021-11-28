# Created by Lauren at 11/24/21
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Search for Anime
    And Click on search icon
    Then Search results have Anime