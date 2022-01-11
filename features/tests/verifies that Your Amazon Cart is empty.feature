# Created by Lauren at 12/7/21
Feature: # Amazon Cart is empty.
  # verifies that Your Amazon Cart is empty.

  Scenario: Verify links an open Amazon Bestsellers
   Given Open Amazon page
    When  User is sign in the homepage
    And Verify that there a 5 links
    And verify if link one is Best sellers
    And verify if link two is New Release
    And verify if link three is Movers & Shakers
    And verify if link four is Most Wished For
    And verify is link five is Gift Ideas
    Then  Click on link one Best sellers