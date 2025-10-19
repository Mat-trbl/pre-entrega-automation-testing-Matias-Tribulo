from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL_page = 'https://www.saucedemo.com/'
login_name = 'standard_user'
login_password = 'secret_sauce'
login_name_box = (By.NAME,"user-name")
login_password_box = (By.NAME,"password")
login_button =(By.ID,"login-button")


def get_driver():
    #Instalacion del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    #time.sleep(2)
    driver.implicitly_wait(5)
    return(driver)

def login(driver):
    driver.get(URL_page)

    #Ingreso de credenciales de login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_name_box)
    ).send_keys(login_name)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_password_box)
    ).send_keys(login_password)
    driver.save_screenshot('login.png')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_button)
    ).click()

