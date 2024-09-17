Feature: Login Functionality
  @login @DataDrivenTesting
  Scenario Outline: Login with credentials
    Given I navigated to Login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
    |email                              |password |
    |testvalidation1234@outlook.com     |lol1234  |
    |testvalidation123423@outlook.com   |lol1234  |
    |testvalidation1234235@outlook.com  |lol1234  |

  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email address and valid password say "lol1234" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email address say "testvalidation1234@outlook.com" and invalid password say "111" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email address and invalid password say "11111" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message
