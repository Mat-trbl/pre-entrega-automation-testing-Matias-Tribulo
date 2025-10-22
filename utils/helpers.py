from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located as EC_presence
import time

URL_page = 'https://www.saucedemo.com/'
login_name = 'standard_user'
login_password = 'secret_sauce'
login_name_box = (By.NAME,"user-name")
login_password_box = (By.NAME,"password")
login_button =(By.ID,"login-button")


def get_driver():

    chrome_options = Options()

    #Instalacion del driver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

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
    driver.save_screenshot('screenshot/login.png')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_button)
    ).click()

def element_selection(driver,element):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(element)
    ).click()

#def is_element_visible(driver, element) -> bool:
#    
#    #Comprueba si un elemento está visible en la página.
#    try:
#        
#        sidebar_menu = driver.find_element(element)
#        style = sidebar_menu.get_attribute("style")
#        print('esto ese', style)
#        assert "-100%" in style
#        return True
#    except TimeoutException:
#        # El elemento no se hizo visible dentro del tiempo de espera.
#        return False
#    except Exception as e:
#        # Manejo de otros posibles errores (e.g., driver error)
#        print(f"Ocurrió un error al verificar la visibilidad de {element}: {e}")
#        return False
