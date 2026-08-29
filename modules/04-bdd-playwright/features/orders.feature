Feature: Order filtering
  Scenario Outline: Filter orders by status
    Given I am signed in to the orders page
    When I filter orders by "<status>"
    Then I see exactly one order with status "<status>"

    Examples:
      | status  |
      | paid    |
      | pending |
      | shipped |

  Scenario: A missing status shows no orders
    Given I am signed in to the orders page
    When I filter orders by "missing"
    Then I see an empty orders message
