class producto:
    tofertas= "Todas las ofertas"
    def __init__(self, nombre, poriginal, poferta, vendedor):
        self.nombre=nombre
        self.poriginal = poriginal
        self.poferta = poferta
        self.vendedor = vendedor
        self.dif=self.poriginal-self.poferta
    def printp(self):
        print( f"Las características del producto son:\n-----------------------------\n"+
        f"Categoría: {self.tofertas}\nNombre: {self.nombre}\nVendedor: {self.vendedor}\nPrecio original: {self.poriginal} $\nPrecio oferta: {self.poferta} $\nDifrencia de precio: {self.dif} $")
        return "-----------------------------"
        
class Plista():
    def pp(self,list):
        for k in range(len(list)):
            print(list[k].printp())
        return ""

p_0= producto('Teléfono',300000,250000,'Huawei')
p_1= producto('Notebook',700000,630000,'Asus')
p_2= producto('Cocina',180000,150000,'Sindelen')
p_3= producto('Tv',290000,240000, 'Samsung')
Lt = [p_0,p_1,p_2,p_3]

l=Plista()
print(l.pp(Lt))
