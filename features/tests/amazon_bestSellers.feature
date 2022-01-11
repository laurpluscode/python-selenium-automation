Feature: # Amazon Cart is empty.
  # verifies that Your Amazon Cart is empty.

  Scenario: # Verify Amazon best sellers links
   Given Open Amazon page
    When User is sign in the homepage
    And Verify if link one is Best sellers
    And Verify if link two is New Release
    And Verify if link three is Movers & Shakers
    And Verify if link four is Most Wished For
   Then Verify is link five is Gift Ideas


