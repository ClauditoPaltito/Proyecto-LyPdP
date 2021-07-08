import random
from time import sleep
from selenium import webdriver
import poo as poo
import funcional as f

def caambio(l):
    p = l[2:len(l)]
    if len(p) >= 5 and len(p) <= 7:
        pr = l[2:len(l)-4]+l[len(l)-3:len(l)]
    elif len(p) > 7 and len(p) <= 11:
        pr = l[2:len(l)-8]+l[len(l)-7:len(l)-4]+l[len(l)-3:len(l)]
    else:
        pr=p
    return(int(pr))

def Scraping():
    path = 'chromedriver.exe'
    website = 'https://www.mercadolibre.cl'
    driver = webdriver.Chrome(path)
    driver.get(website)
    driver.set_window_size(1920, 1080)
    ofertas_button = driver.find_element_by_xpath('//a[@href="https://www.mercadolibre.cl/ofertas#nav-header"]')
    ofertas_button.click()
    sleep(random.uniform(0.5, 1.5))
    Lista = []
    for i in range(18):
        if i == 6 or i == 12:
            sig = driver.find_element_by_xpath('//button[@class="next-button "]')
            sig.click()
            sleep(random.uniform(0.5, 1.5))

        sec = driver.find_element_by_xpath(f'//div[@data-index="{i}"]')
        sec.click()
        sleep(random.uniform(1, 2))
        productos = driver.find_elements_by_xpath('//li[@class="promotion-item"]')
        lista=[]
        for product in productos:
            precioOR = product.find_element_by_xpath('.//span[@class="promotion-item__oldprice"]').text
            precioOF = product.find_element_by_xpath('.//div[@class="promotion-item__price-block"]/span[@class="promotion-item__price"]/span').text
            titulo = product.find_element_by_xpath('.//p[@class="promotion-item__title"]').text
            tof = driver.find_element_by_xpath('//div[@class="carousel_item selected"]').text
            prod = poo.producto(titulo,caambio(precioOR),caambio(precioOF),tof)
            lista.append(prod)
        Lista.append(lista)
    driver.quit()
    return Lista

scrap = Scraping()
print("\nCantidad de categorías: ",len(scrap))


print("\nCantidad de productos en la primera página de cada categoría:")
for i in range(len(scrap)):
    print(f"{scrap[i][0].tofertas}: {len(scrap[i])}")


for i in range(len(scrap)):
    print("\nCategoría: ",f.print_ofertas_categoria(scrap)[i][0],"\nPocercentaje promedio de descuento: ",f.print_ofertas_categoria(scrap)[i][1],"%")


print("\nPromedio generál del procentaje de descuento",f.prom_ofertas_total(scrap))


list_ord = f.top_ofertas_listas(scrap)
print("\nCaracterísticas de los productos con mayor porcentaje de descuento por categoría:")
for i in range(len(list_ord)):
    print(list_ord[i][-1].printp())


list_list_ord=f.bestsort(list_ord)
print("\nCaracterísticas del producto con el mayor porcentaje de descuento es:")
print(list_list_ord[-1].printp())

###### TODOS LOS FOR PASARLOS A FUNCIONES ########