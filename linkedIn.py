from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Preferences for the website options.
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         'useAutomationExtension': False,
         'disable-infobard': True}

#Adding the preferences to the webdriver.
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", prefs)
#Specifying the drivers path, easiest way is to just have the driver in the same folder as your python script!
driver = webdriver.Chrome(chrome_options=options, executable_path=r'.\chromedriver')


#Submit button can usually be ignored by just adding "Keys.Enter" after password.
#This can be handy because sometimes the website might not have a real Id or tag for the Submit button!
#I still left the submit_buttonId parameter there just for illustration and as an example.

def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password + Keys.ENTER)
   driver.find_element_by_id(submit_buttonId).click()

driver.maximize_window()
login("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin", "username", "yourEmail/yourPhone", "password", "yourPassword", "login-submit")


