
Feature: Target authentication

  Scenario: Logged out user can sign in
    Given open target main page
    When  click sign in
    And click Sign In after it opens right side navigation menu
    Then  sign In form opens