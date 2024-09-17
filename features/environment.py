import allure
from selenium import webdriver
from utilities import ConfigReader


# the next functions are hooks that helps the code to be clean
def before_scenario(context,driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.browser = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.browser = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.browser = webdriver.Edge()
    elif browser_name.__eq__("safari"):
        context.browser = webdriver.Safari()
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name = "screenshot_failed",
                      attachment_type=allure.attachment_type.PNG)
