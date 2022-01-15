# Created by lauren at 1/11/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Hovers over New Arrivals, then verifies that the user sees the deals.
    Given Open Amazon page
    Then Go to 'New Arrivals'
    And verifies that the user sees the deals.