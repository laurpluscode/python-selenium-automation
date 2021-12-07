# Created by Lauren at 12/7/21
Feature: # Amazon Cart is empty.
  # verifies that Your Amazon Cart is empty.

  Scenario: # Enter scenario name here
   Given Open Amazon page
    When  User is sign in the homepage
    And Click on the shopping  cart
    Then  Cart results for items in the cart are shown