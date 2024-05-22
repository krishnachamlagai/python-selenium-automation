
Feature: # Target cart tests

  Scenario: # Target cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Your cart is empty message is shown

  Scenario: # Add product into cart and verify it's there
    Given Navigate to Given Product Page
    When Click on Add To Cart
    Given Navigate to Cart Page
    Then Verify given product is present in the cart

