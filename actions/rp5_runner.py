from drivers import driver
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as conditions
from selenium.webdriver.common.by import By
import properties

ACTION_MENU_DELETE_MENU_ITEM = "//*[contains(@class, 'ghostMenuButton') and child::*[contains(text(), 'Delete')]]"

LAUNCH_CHECKBOX_XPATH = "//*[contains(@class , 'checkboxCell')]//div"

ACTIONS_MENU_XPATH = "//*[contains(@class, 'ghostMenuButton')]"

PASSWORD_BUTTON_XPATH = "//*[@placeholder='Password']"

LOGIN_BUTTON_XPATH = "//*[@placeholder='Login']"

DELETE_CONFIRM_BUTTON_XPATH = "//*[contains(@class, 'bigButton__color-tomato')]"

HAM_DELETE_BUTTON_XPATH = "//*[contains(@class, 'hamburgerMenuItem') and contains(text(), 'Delete')]"

HAMBURGER_XPATH = "//*[contains(@class , 'launchSuite')]//*[contains(@class, 'hamburger__hamburger___')]"


class Rp5Runner:

    def __init__(self):
        self.driver = driver.DriverManager.get_driver()
        self.driver.implicitly_wait(30)
        self.driver.get(properties.RP_PATH_TO_OLD_LAUNCHES_FILTER)

    def auth(self, login=properties.RP_LOGIN, pwd=properties.RP_PASSWORD):
        self.driver.find_element_by_xpath(LOGIN_BUTTON_XPATH).send_keys(login)
        self.driver.find_element_by_xpath(PASSWORD_BUTTON_XPATH).send_keys(pwd + keys.Keys.ENTER)
        self.__wait_until_ham_visible()

    def delete_last_launch(self):
        self.__wait_until_element_clickable(HAMBURGER_XPATH)
        self.driver.find_element_by_xpath(HAMBURGER_XPATH).click()
        self.driver.find_element_by_xpath(HAM_DELETE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(DELETE_CONFIRM_BUTTON_XPATH).click()
        self.__wait_until_ham_visible()

    def delete_first_n_launches_on_page(self, amount):
        self.__wait_until_element_clickable(HAMBURGER_XPATH)
        launch_checkboxes = self.driver.find_elements_by_xpath(LAUNCH_CHECKBOX_XPATH)
        for item in range(0, amount):
            launch_checkboxes[item].click()
        self.driver.find_element_by_xpath(ACTIONS_MENU_XPATH).click()
        self.driver.find_element_by_xpath(ACTION_MENU_DELETE_MENU_ITEM).click()
        self.driver.find_element_by_xpath(DELETE_CONFIRM_BUTTON_XPATH).click()
        self.__wait_until_ham_visible()

    def __wait_until_ham_visible(self):
        WebDriverWait(self.driver, 60).until(lambda x: 0 < len(self.driver.find_elements_by_xpath(HAMBURGER_XPATH)))

    def __wait_until_element_clickable(self, element_locator):
        WebDriverWait(self.driver, 60).until(conditions.element_to_be_clickable((By.XPATH, element_locator)))
