Feature: Target Product Search

  Scenario Outline: User can search for a product
    Given Open Target main page
    When input <search_query> into target search field
    And Click on Target search icon
    Then Product results for <results> are shown on target page


    Examples:
      | search_query | results     |
      | coffee       | "coffee"    |
      | socks        | "socks"     |
      | iphone 15    | "iphone 15" |