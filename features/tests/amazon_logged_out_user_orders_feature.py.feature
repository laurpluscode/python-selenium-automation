# Created by Lauren at 11/27/21
Feature: # Enter feature name here
  # Enter feature description here
  # Logged out user sees Sign in page when clicking Orders

  Scenario: # Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    And Verify Sign in page opened
    Then results are Logged out users can sees Sign in page when clicking Orders
