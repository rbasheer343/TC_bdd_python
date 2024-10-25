@given("User is on BestBuy page")
def step_impl():
  Browsers.Item[btChrome].Navigate(Project.Variables.testUrl)
  
@when("User clicks on myAccount option")
def step_impl():
  browser = Aliases.browser
  browser.pageBestBuyShopOnline.linkMyBestBuyAccount.Click()

@when("User enters valid username and password")
def step_impl():
  browser = Aliases.browser
  emailInput = browser.pageSignin.formSignin.emailinputEmailAddress
  emailInput.SetText(Project.Variables.userName)
  passwordBox= browser.pageSignin.formSignin.passwordboxPassword
  passwordBox.SetText(Project.Variables.Password1)

@when("User clicks on login button")
def step_impl():
  browser = Aliases.browser
  browser.pageSignin.formSignin.buttonSignIn.ClickButton()

@then("Welcome message is displayed")
def step_impl():
  welcomeMsg=Aliases.browser.pageEnCa.accountGreetings.textnodeWelcomeToMyBestBuy.innerText
  Log.Message(welcomeMsg)
  aqObject.CheckProperty(Aliases.browser.pageEnCa.accountGreetings.textnodeWelcomeToMyBestBuy, "contentText", cmpEqual, "Welcome to My Best Buy.")

@when("User enters invalid {arg} and {arg}")
def step_impl(param1, param2):
  browser = Aliases.browser
  emailInput = browser.pageSignin.formSignin.emailinputEmailAddress
  emailInput.SetText(param1)
  passwordBox= browser.pageSignin.formSignin.passwordboxPassword
  passwordBox.SetText(param2)

@then("The Login screen should display proper {arg} for each {arg}")
def step_impl(param1, param2):
  Log.Message("param1 "+param1)
  Log.Message("param2 "+param2)
  browser = Aliases.browser
  if param2 == "email":
    aqObject.CheckProperty(browser.pageSignin.formSignin.panelPleaseEnterAValidEmail, "contentText", cmpEqual,param1.strip() )
  elif param2 == "password":
    aqObject.CheckProperty(browser.pageSignin.formSignin.panelPleaseEnterYourPasswordIt, "contentText", cmpEqual,param1.strip() )
  elif param2 == "common":
      aqObject.CheckProperty(browser.pageSignin.formSignin.textnodeSorryTheEMailAddressAnd, "contentText", cmpEqual,param1.strip() )
  else:
      Log.Message("Invalid option sent to validate on error")
