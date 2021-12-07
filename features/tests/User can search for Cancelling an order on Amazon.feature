# Created by Lauren at 12/7/21
Feature: # User can search for Cancelling an order on Amazon

  Scenario: # Enter scenario name here
   Given Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
    When  Use “Search Help Library” field and search for Cancel order:
    And Click on search Cancel orders/items
    Then Search results for cancel items/orders are shown
