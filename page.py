import time,logging
from selenium.common.exceptions import NoAlertPresentException 
from Exceptions import NoElementAvailableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

"""
==============================================================================================================================
 This is the basic page which contains common modules for all pages. base page inherets from this page
==============================================================================================================================

"""""
#setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class page (object):
    timeout_seconds = 20
    
    def __init__(self,driver):
        self.driver = driver
        logger.info("driver intialized")
        
    def find_element_by_locator(self,locator):
        return self.driver.find_element_by_locator(locator)
    
    def find_elements_by_locator(self,locator):
        return self.driver.find_elements_by_locator(locator)
    
    def enter_text(self,locator,text):
        element = self.driver.find_element_by_locator(locator)
        element.send_keys(text)
        
    def click_button(self,locator):
        self.find_element_by_locator(locator).click()
        
    def Send_Enter(self,locator):
        self.find_element_by_locator(locator).send_keys(Keys.ENTER)
        
    #wait for element waits until the element is present on the screen or till time out is reached    
    def wait_for_element(self,locator):
        for i in range (self.timeout_seconds):
            if self.driver.is_element_present(locator):
                break
            time.sleep(.5)
        else:
               raise  NoElementAvailableException () 
               logger.exception("Wait for element " + str(locator)+" timed out")
               return False 
        return True
    
    #wait for element waits until the element for mail is present on the screen or till time out is reached  
    def wait_for_mail(self,locator):
        logger.info("executing to find if mail is available")
        for i in range (self.timeout_seconds):
            if self.driver.is_element_available(locator):
                logger.info("mail is found")
                break
            logger.info("sleeping to find the mail identified by locator =  " + str(locator))
            time.sleep(.5)
        else:
               raise  NoElementAvailableException () 
               logger.exception("NO Build Today... Exiting")
               return False
        return True
    
    #wait for the hidden element to be present on the screen    
    def wait_for_hidden(self,locator):
        for i in range (self.timeout_seconds):
            if self.driver.is_element_present(locator):
                logger.info("sleeping to find the element identified by locator = " + str(locator))
                time.sleep(.5)
            else:
                break
            
        else :
            raise NoElementAvailableException ()
            logger.exception("Wait for the hidden element timed out")
        return True
    
    def Accept_alert(self):
        for i in range (self.timeout_seconds):
            logger.debug("before_try_")
            try:
                logger.debug("Inside try wait alert")
                jalert = self.driver.switch_to.alert
                logger.info("switched to alert")
                jalert.accept()
                logger.info("alert accepted")
                return 
            except NoAlertPresentException as nape:
                logger.warning("alert not seen , sleeping till alert is shown")
            time.sleep(.5)
        else:
            logger.debug("inside else")
            raise NoAlertPresentException ()
        logger.exception("no alert observed , returing")
        return True
    
    #used to navigate from the current window to newly created window. 
    def switch_to_desired_window(self):
        window_handle_names = self.driver.window_handles
        if len(window_handle_names) == 1 :
            return
        else:
            self.driver.switch_to_window(window_handle_names[1])
            self.driver.current_window_handle
            return
        
    #Once mail is sent the new pop up window closes, this part confirms the closure of the window    
    def confirm_mail_sent(self):
        window_handles_names = []
        for i in range(self.timeout_seconds):
            window_handles_names[:] = []
            window_handles_names = self.driver.window_handles
            if len(window_handles_names) == 1:
                self.driver.switch_to_window(window_handles_names[0])
                logger.info("mail sent confirmed")
                return 
            else:
                logger.info("waiting for mail to be sent")
                time.sleep(.5)
            
    
    def print_the_current_window_handle(self):
        logger.debug(self.driver.current_window_handle)
        return 
            
            
                