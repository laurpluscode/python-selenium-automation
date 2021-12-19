# Created by Lauren at 11/24/21
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Search for Anime
    And Click on search icon
    Then Search results have Anime


    Scenario Outline: User can search for a product on Amazon2
      Given Open Amazon page
      When Search for <product>
      And Click search icon
      Then Search results have <expected_result>

      Examples:
      |product |expected_results |
      |Anime   |"Anime"          |
      |Ring    |"ring"           |

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Anime
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product