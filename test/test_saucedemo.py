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
     title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
     print(title)
     assert title == 'Products'



