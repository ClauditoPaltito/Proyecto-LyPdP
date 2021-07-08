from functools import reduce

def sort(lista):
    lista2=[]
    lista2.append(reduce((lambda x,y:x if x.pors<y.pors else y), lista))
    lista.remove(reduce((lambda x,y:x if x.pors<y.pors else y), lista))
    lista=[i for i in lista2]
    return ((reduce((lambda x,y:x if x.pors<y.pors else y), lista)))

def top(lista):
    return [sort(lista) for x in range(len(lista))]

def top_ofertas_listas(lista_listas):
  return [top(x) for x in lista_listas]

def best(lista_listas):
    return [x.pop() for x in lista_listas]

def bestsort(lista_listas):
    return top(best(lista_listas))


#Printear promedio total de ofertas
def suma_ofertas_categorias(lista):
  suma_porcentajes_categoria=reduce(lambda acum,x: acum + x.pors,lista, 0)
  cant_datos=len(lista)
  return [suma_porcentajes_categoria,cant_datos]
def prom_ofertas_total(lista_listas):
  return round((reduce(lambda acum,x: acum + (suma_ofertas_categorias(x)[0]),lista_listas, 0))/(reduce(lambda acumm,y: acumm + (suma_ofertas_categorias(y)[1]),lista_listas, 0)),2)

#Printear promedio por categorias
def prom_ofertas_categoria(lista):
  suma_porcentajes_categoria=reduce(lambda acum,x: acum + x.pors,lista, 0)
  cant_datos=len(lista)
  prom_categoria=suma_porcentajes_categoria/cant_datos
  return prom_categoria
def print_ofertas_categoria(lista_listas):
  lista_ofertas_categorias=[[x[0].tofertas,prom_ofertas_categoria(x)] for x in lista_listas]
  return [[x[0],round(x[1],2)] for x in lista_ofertas_categorias]
