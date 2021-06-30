from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd
from os import path
import time

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,800")


# Temas: Localizar un boton, seleccionar elemento de listas desplegables y extraer datos de tabla

# definer pagina a scrapear y ruta donde descargaste chromediver
website = 'https://www.mercadolibre.cl/'
path = 'chromedriver.exe'


# definer variable 'driver'
driver = webdriver.Chrome(path)

# abrir Google Chrome mediante chromedriver
driver.get(website)

driver.set_window_size(1920, 1080)
size = driver.get_window_size()
print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))

# localizar un botón
ofertas_button = driver.find_element_by_xpath('//a[@href="https://www.mercadolibre.cl/ofertas#nav-header"]')
# dar click en un botón
ofertas_button.click()

# # usar una sección como referencia para garantizar que vamos a encontrar el elemento que buscamos (util cuando no hay id y queremos evitar nombre de clases repetitivos)
# caja = driver.find_element_by_class_name('panel-body')
# # seleccionar dropdown y seleccionar por texto
# dropdown = Select(caja.find_element_by_id('country'))
# dropdown.select_by_visible_text('Spain')
# # wait implicito (util cuando la página demora en cargar elemetos varios segundos y obtenemor el error "ElementNotVisibleException")
# time.sleep(5)
# # seleccionar elementos de la tabla
# matches = driver.find_elements_by_css_selector('tr')

# # almacenar en listar
# partidos = [match.text for match in matches]

# #cerrar Google Chrome abierto por chromedriver
# driver.quit()

# # Bonus: Crea Dataframe en Pandas y exporta data en CSV (Excel)
# df = pd.DataFrame({'goals': partidos})
# print(df)
# df.to_csv('tutorial.csv', index=False)