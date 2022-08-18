
from selenium.webdriver.support.events import AbstractEventListener
from pom.authorization import HomePageNavAuthorization

class MyListener(AbstractEventListener):
    def after_find(self, by, value, driver):
        HomePageNavAuthorization(driver).get_nav_link_my_maze().click()
        HomePageNavAuthorization(driver).get_nav_link_mail().clear()



    # def after_navigate_to(self, url, driver):
    #     print("After navigate to %s" % url)