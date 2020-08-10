import npyscreen
import sys

# Without a `MAIN` form, this generates an exception

class myEmployeeForm(npyscreen.Form):
  def create(self):
    self.myName = self.add(npyscreen.TitleText, name='Name')
    self.myDept = self.add(
      npyscreen.TitleSelectOne, 
      name='Department',
      max_height=11,
      scroll_exit=True,
      values = sorted([
        'Censorship and documents'
        'Field experimental unit', 
        'Foreign nationalities',
        'Maritime unit',
        'Morale operations', 
        'Operational group command',
        'Research and analysis', 
        'Secret intelligence', 
        'Special operations', 
        'Special projects', 
        'X-2', 
      ]))
    self.myDate = self.add(npyscreen.TitleDateCombo, name='Date employed')

  # Necessary to allow exiting the application
  def afterEditing(self):
    self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
  def onStart(self):
    self.addForm('MAIN', myEmployeeForm, name='New Employee')

if __name__ == '__main__':
  try:
    App().run()
  except KeyboardInterrupt:
    sys.exit(0)