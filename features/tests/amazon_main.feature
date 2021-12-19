# Created by Lauren at 12/18/21
Feature: Test for Amazon main page

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify Anime menu present

    Scenario: User can see 40 footer links
      Given Open Amazon page
      Then Verify 40 links present

      Scenario: Sign in page can be opened from Sign in popup
        Given Open Amazon page
        When Click Sign In from popup
        Then Verify Sign In page opens