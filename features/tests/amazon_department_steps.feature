# Created by Lauren at 1/11/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Using a dropdown; search for an item in a different Amazon department.
    Given Open Amazon page
     When User is sign in the homepage
      Then Navigate to the "All" tab next to the search box
      And Use the dropdown menu to choose the 'Books' department
