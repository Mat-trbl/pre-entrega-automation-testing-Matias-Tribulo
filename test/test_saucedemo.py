import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from utils.helpers import get_driver, login

@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):
     login(driver)
     driver.save_screenshot('intro.png')
     # validacion del ingreso a la pagina de inventario
     assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
     # validacion del titulo de la pagina del inventario
     logo = driver.find_element(By.CSS_SELECTOR,"div.primary_header .app_logo").text
     assert logo == 'Swag Labs'
     title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
     assert title == 'Products'

def test_catalogo(driver):
     # logueo de la pagina
     login(driver)
     # validacion del titulo de la pagina del inventario
     title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
     assert title == 'Products'
     # verifico que la pagina contenga al menos un producto
     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
     assert len(products) > 0
     # verifico la estructura de la pagina
     

