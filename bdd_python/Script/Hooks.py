import commonMethods

@beforefeature
def someFunc(feature):
  # Perform some action before running a feature file, for example:
  Log.Message("Before running the " + feature.Name + "feature file")

  
@afterfeature
def someFunc(feature):
  # Perform some action after executing a feature file, for example:
  Log.Message("The " + feature.Name + " feature file has been executed")


@beforescenario
def someFunc(scenario):
  # Perform some action before running a scenario, for example:
  try:
      Log.Message("Before running the " + scenario.Name + "scenario")
      if scenario.Tags.Contains("@skipLogin"):
        Log.Message("Skipping login for this scenario")
        return
      commonMethods.login()
  except Exception as e:
          Log.Message(f"Error checking tags: {str(e)}")
  
@afterscenario
def someFunc(scenario):
  # Perform some action after executing a scenario, for example:
  Log.Message("The " + scenario.Name + " scenario has been executed")
  try:
      if scenario.Tags.Contains("@negativelogin"):
        Log.Message("Skipping logout for this scenario")
        return
      commonMethods.logout()
  except Exception as e:
          Log.Message(f"Error checking tags: {str(e)}")
  