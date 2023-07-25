Feature: Flipkart website

   # Test Case 1
  Scenario: Validate Flipkart site product search functionality
    Given launch the browser
    When open flipkart website
    Then search for dell laptop
    And select Dell laptop
    Then In Dell product detail page get the product title
    And close the browser


  Scenario Outline: Validate Flipkart site product search functionality with examples
    Given launch the browser
    When open flipkart website
    Then search for "<searchkeyword>"
    Then verify search results based on "<searchkeyword>"
    And select checkbox filter
    Examples:
      | searchkeyword |
      |Hp laptops   |
      |Shoes for men|
