class producto:
    def __init__(self, nombre, poriginal, poferta, tipo):
        self.tofertas = tipo
        self.nombre=nombre
        self.poriginal = poriginal
        self.poferta = poferta
        self.dif=self.poriginal-self.poferta
        self.pors=round((self.dif*100)/self.poriginal,2)
    def printp(self):
        print("-----------------------------\n"+
        f"Categoría: {self.tofertas}\nNombre: {self.nombre}\nPrecio original: ${self.poriginal}\nPrecio oferta: ${self.poferta}\nDifrencia de precio: ${self.dif}\nPorcentaje de descuento: {self.pors}%")
        return "-----------------------------"
        
class Plista():
    def pp(self,list):
        for k in range(len(list)):
            print(list[k].printp())
        return ""

# p_0= producto('Teléfono',300000,250000,'Huawei')
# p_1= producto('Notebook',700000,630000,'Asus')
# p_2= producto('Cocina',180000,150000,'Sindelen')
# p_3= producto('Tv',290000,240000, 'Samsung')
# Lt = [p_0,p_1,p_2,p_3]

# print(p_0.pors)

# l=Plista()
# print(l.pp(Lt))
