from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging as logger

import pytest

user_name = 'Pawan7593'
key = 'ZqUuuwHmf7zGkrte88kDIMw1fL2sSDpJxvNcDVCAvjD3QktycK'
chrome_options = ChromeOptions()
chrome_options.browser_version = "86.0"
chrome_options.platform_name = "Windows 10"
lt_options = {}
lt_options["username"] = "Pawan7593"
lt_options["accessKey"] = "ZqUuuwHmf7zGkrte88kDIMw1fL2sSDpJxvNcDVCAvjD3QktycK"
lt_options["visual"] = True
lt_options["video"] = True
lt_options["build"] = "Selenium Advance Chrome"
lt_options["project"] = "Selenium Advance Chrometled"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
chrome_options.set_capability('LT:Options', lt_options)

edge_options = EdgeOptions()
edge_options.browser_version = "87.0"
edge_options.platform_name = "macOS Sierra"
lt_options = {}
lt_options["username"] = "Pawan7593"
lt_options["accessKey"] = "ZqUuuwHmf7zGkrte88kDIMw1fL2sSDpJxvNcDVCAvjD3QktycK"
lt_options["visual"] = True
lt_options["video"] = True
lt_options["build"] = "Selenium Advance Edge"
lt_options["project"] = "Selenium Advance edge"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
edge_options.set_capability('LT:Options', lt_options)

@pytest.mark.Chrome
def test_selenium_with_chrome():
    remote_url = "https://" + user_name + ":" + key + "@hub.lambdatest.com/wd/hub"
    # web_driver = webdriver.Chrome()
    driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
    driver.execute_script('lambda-name=seleniumAdvance_with_chrome_window')
    driver.get("https://www.lambdatest.com/")
    driver.maximize_window()
    # WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located("//a[normalize-space()='See All Integrations']"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='See All Integrations']")))
    scroll_element = driver.find_element(By.XPATH, "//a[normalize-space()='See All Integrations']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_element)
    scroll_down = driver.find_element(By.CSS_SELECTOR,
                                      "h2[class='text-shadow text-size-40 font-bold tracking-wide leading-tight text-black mb-20 text-center smtablet:text-size-30']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down)
    ActionChains(driver).key_down(Keys.CONTROL).click(scroll_element).key_up(Keys.CONTROL).perform()
    window_no = driver.window_handles
    logger.info(window_no)
    driver.switch_to.window(driver.window_handles[1])
    new_tab_url = driver.current_url
    assert new_tab_url == 'https://www.lambdatest.com/integrations', f"New tab url is not same"
    scroll_down_next = driver.find_element(By.XPATH,
                                           "//div[@id='codeless_row']//h2[@class='text-size-24 font-semibold m-2']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down_next)
    scroll_down_next_2 = driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]/h3')
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down_next_2)
    driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]/a').click()
    next_page_title = driver.title
    assert next_page_title == 'Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest', f'Title is not same'
    logger.info(next_page_title)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    window_no = driver.window_handles
    logger.info(len(window_no))
    driver.get('https://www.lambdatest.com/blog')
    driver.find_element(By.LINK_TEXT, 'Community').click()
    current_url = driver.current_url
    assert current_url == 'https://community.lambdatest.com/', f'Current url is not same as expected'
    driver.execute_script("lambda-status=passed")
    driver.quit()


@pytest.mark.test
def test_seleniumAdvance_with_mac_edge():
    remote_url = "https://" + user_name + ":" + key + "@hub.lambdatest.com/wd/hub"
    # web_driver = webdriver.Chrome()
    driver = webdriver.Remote(command_executor=remote_url ,options=edge_options)
    driver.execute_script('lambda-name=seleniumAdvance_with_mac_edge')
    driver.get("https://www.lambdatest.com/")
    driver.maximize_window()
    # WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located("//a[normalize-space()='See All Integrations']"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='See All Integrations']")))
    scroll_element = driver.find_element(By.XPATH, "//a[normalize-space()='See All Integrations']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_element)
    scroll_down = driver.find_element(By.CSS_SELECTOR,
                                      "h2[class='text-shadow text-size-40 font-bold tracking-wide leading-tight text-black mb-20 text-center smtablet:text-size-30']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down)
    ActionChains(driver).key_down(Keys.CONTROL).click(scroll_element).key_up(Keys.CONTROL).perform()
    window_no = driver.window_handles
    logger.info(window_no)
    driver.switch_to.window(driver.window_handles[1])
    new_tab_url = driver.current_url
    assert new_tab_url == 'https://www.lambdatest.com/integrations', f"New tab url is not same"
    scroll_down_next = driver.find_element(By.XPATH,
                                           "//div[@id='codeless_row']//h2[@class='text-size-24 font-semibold m-2']")
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down_next)
    scroll_down_next_2 = driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]/h3')
    driver.execute_script("arguments[0].scrollIntoView()", scroll_down_next_2)
    driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]/a').click()
    next_page_title = driver.title
    assert next_page_title == 'Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest', f'Title is not same'
    logger.info(next_page_title)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    window_no = driver.window_handles
    logger.info(len(window_no))
    driver.get('https://www.lambdatest.com/blog')
    driver.find_element(By.LINK_TEXT, 'Community').click()
    current_url = driver.current_url
    assert current_url == 'https://community.lambdatest.com/', f'Current url is not same as expected'
    driver.execute_script("lambda-status=passed")
    driver.quit()
