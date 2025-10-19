from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

URL_page = 'https://www.saucedemo.com/'
login_name = 'standard_user'
login_password = 'secret_sauce'


def get_driver():
    #Instalacion del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    time.sleep(2)
    return(driver)

def login(driver):
    driver.get(URL_page)

    #Ingreso de datos de login
    login_name_box = driver.find_element(By.NAME,"user-name")
    login_name_box.send_keys(login_name)
    login_password_box = driver.find_element(By.NAME,"password")
    login_password_box.send_keys(login_password)
    driver.save_screenshot('login.png')

    time.sleep(2)

    login_button = driver.find_element(By.ID,"login-button")
    login_button.click()

    time.sleep(2)
