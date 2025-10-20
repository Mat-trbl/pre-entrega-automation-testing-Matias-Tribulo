import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import time


from utils.helpers import get_driver, login, element_selection


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
     print('el contenido del menu es de:', len(products))
    
     # verifico la estructura de la pagina
     #element = (By.CLASS_NAME, "bm-menu-wrap")
     #is_element_visible(driver,element)
     #element = (By.ID,'react-burger-menu-btn')
     #element_selection(driver,element)
     #time.sleep(2)
     #driver.save_screenshot('menu.png')

     #element = (By.ID, 'bm-menu-wrap')
     #is_element_visible(driver,element)
     #menu = driver.find_elements(By.CLASS_NAME, 'bm-menu')

def test_carrito(driver):
     # logueo de la pagina
     login(driver)
     # seleccionar producto y agreagra a carrito
     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
     element = products[0].find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
     chosen_product = products[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
     print('el producto es', chosen_product)
     element_selection(driver,element)
     time.sleep(5)
     driver.save_screenshot('carrito.png')
     # compruebo que se agrego el, producto al carritoctiomn
     badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
     assert badge > "0"
     # abrir carrito
     element_p = (By.CLASS_NAME, "shopping_cart_link")
     element_selection(driver,element_p)
     assert driver.current_url == 'https://www.saucedemo.com/cart.html'
     # comprobar el producto agregado
     cart_item = driver.find_elements(By.CLASS_NAME, 'cart_list')
     cart_item_name = cart_item[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
     assert chosen_product == cart_item_name





