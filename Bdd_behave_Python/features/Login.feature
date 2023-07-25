Feature: Flipkart website

   # Test Case 1
  Scenario: Validate Flipkart site Functionality
    Given launch the browser
    When open flipkart website
    Then search for dell laptop
    And select Dell laptop
    Then In Dell product detail page get the product title
    And close the browser


  Scenario Outline:
        Given launch the browser
    When open flipkart website
    Then search for "<searchkeyword>"
    And select processor checkbox filter
    Examples:
      | searchkeyword |
      |Hp laptops   |
