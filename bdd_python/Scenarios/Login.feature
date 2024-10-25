Feature: Login

  @skipLogin
  Scenario: Successfull Login to BestBuy 
    Given User is on BestBuy page
    When User clicks on myAccount option
    And User enters valid username and password
    And User clicks on login button
    Then Welcome message is displayed
    
  @skipLogin @negativelogin
  Scenario Outline: negative scenarios login
   Given User is on BestBuy page
   When User clicks on myAccount option
   And User enters invalid "<userName>" and "<password>"
   And User clicks on login button
   Then The Login screen should display proper "<message>" for each "<errortype>" 
   
   Examples:
     | userName             | password    | message                                                                                                   | errortype |
     | reshmab@nousinfo.com | xyzhjhjhkhk | Sorry, the e-mail address and password you entered don’t match. Please try again.                         | common    |
     | john11               |             | Please enter a valid email address.                                                                       | email     |
     | kira12@test.com      |             | Please enter your password. It must be 6 to 30 characters and contain at least one number and one letter. | password  |
     | jack15@test.com      | xyz         | Please enter your password. It must be 6 to 30 characters and contain at least one number and one letter. | password  |
   