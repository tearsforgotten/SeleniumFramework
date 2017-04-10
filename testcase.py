from driver import Webdriver
import unittest,time
from base import Login_page
from baselogging import *

"""
==============================================================================================================================
 This is the main test case script. All test cases are added as test cases in unittest and executed accordingly 
==============================================================================================================================

"""""
desired_capabilities = { 'browserName' : 'chrome' }
command_executor = "http://127.0.0.1:4444/wd/hub"



#Unittest code 
class testing_first_code(unittest.TestCase):
    def setUp (self):
        self.driver = Webdriver(desired_capabilities=desired_capabilities, command_executor=command_executor)
        log.info("setup done" )
        #self.current_setUp_name =  setUp.__name__

    def tearDown (self):
        self.driver.close()
        self.driver.quit()
        log.info("tear down done, closed driver")
    
    #Test case for logging in and sending mail    
    def test_enter_login_cred(self):
        log.info("starting first test--> opening url")
        gmail = Login_page(self.driver).open()
        gmail.login()
        gmail.send_mail()
        
        
if __name__ == "__main__":
    unittest.main()
    