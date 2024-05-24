Feature: Target Product Details

  Scenario Outline: User can select colors for a product
    Given Open Target Product <product_id>
    Then Verify user can click through colors
    Examples:
      | product_id |
      | A-91511634 |
      | A-91511634 |
