
Feature: # Target cart tests

  Scenario: # Target cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Your cart is empty message is shown
