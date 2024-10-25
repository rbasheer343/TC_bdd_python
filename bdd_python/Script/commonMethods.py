def login():
  Browsers.Item[btChrome].Navigate(Project.Variables.testUrl)
  browser = Aliases.browser
  emailInput = browser.pageSignin.formSignin.emailinputEmailAddress
  emailInput.SetText(Project.Variables.userName)
  passwordBox= browser.pageSignin.formSignin.passwordboxPassword
  passwordBox.SetText(Project.Variables.Password1)
  browser.pageSignin.formSignin.buttonSignIn.ClickButton()
  
  
def logout():
  page=Aliases.browser.pageEnCa
  page.textnodeUser.Click()
  page.accountMenu.textnodeSignOut.Click()
  Aliases.browser.Close()
  
  
def transformToTable(rawData):
  table = []
  for i in range(1, rawData.RowCount):
    row = rowValues()
    row.name = rawData.Value[i, 0]
    row.password = rawData.Value[i, 1]
    row.message = rawData.Value[i, 2]
    row.actualMessage=""
    table.append(row)
  return table