# Created by rajch at 23.01.2023
Feature: Search
  # Enter feature description here

  Scenario: Check price
    Given I'm logged in
    When I add product to basket
    Then I see price 123