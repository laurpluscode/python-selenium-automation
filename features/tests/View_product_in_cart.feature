# Created by Lauren at 12/7/21
Feature: # Amazon Cart contains products
  # verifies that Your product is in  Amazon Cart

  Scenario: # Enter scenario name here
   Given Open Amazon page
    When  User is sign in the homepage
    And Search "Clean Code" item and add to Cart
    Then  Cart results for "Clean Code" item in the cart are shown