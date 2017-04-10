from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from page import page
from timecheck import Find_Time
import timecheck,logging
import time
import Readconfig_file


"""
==============================================================================================================================
 This is the base page on which testing is done. All the base pages are meant to be inherited from 'page.py' which contains all 
 methods common for all modules
==============================================================================================================================

"""""

#setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

page_url = "https://www.gmail.com"


"""This part reads the configuration file and sets this values into the corresponding dictionary. Range and indexes are depended 
on the number of sections that are to be imported """

locators = {}
Credentials = {}
Email_data = {}
dic = [ {} for _ in range(3)]

for i in range(3):
    dic[i] = Readconfig_file.get_values_from_configfile(i)
locators = dic[0]
Credentials = dic[1]
Email_data = dic[2]
logger.info("created all dictionaries for locators, credentials and emails")

    

#base page on which testing is done
#For the time being all execution are put inside search mail. This will be modified in later commits
class Login_page(page):
                
    def open(self):
        self.driver.get(page_url)
        logger.info("opening page " + str(page_url))
        self.driver.maximize_window()
        if self.wait_for_element (locators['login_email']):
            return self
        else :
            logger.exception ("test failed")
            exit
    
    def login(self):
        self.enter_text(locators['login_email'],Credentials['login'])
        self.click_button(locators['email_next'])
        self.wait_for_element(locators['login_password'])
        self.enter_text(locators['login_password'],Credentials['password'])
        self.click_button(locators['sign_in'])
        logger.info("need to search for " + locators['compose'])
        self.wait_for_element(locators['compose'])
        logger.info("Logged into gmail")
        
        
    def send_mail(self):
        self.click_button(locators['compose'])
        self.enter_text(locators['to'],Email_data['to_mail'])
        self.enter_text(locators['subject'],Email_data['subject'])
        body_element = self.find_element_by_locator(locators['body'])
        #using execute script as Send_Keys method cannot send values to the gmail body
        self.driver.execute_script("arguments[0].innerHTML = arguments[1];", body_element, Email_data['body']);
        self.click_button(locators['send'])
        logger.info("mail have been sent")
        
   
            
            
            
        
        
