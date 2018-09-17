__author__ = 'Daniel Garcia'

from memoria_estatica import *


Panaderia = ['Conchas','Chilindrina','Cuernitos']
Precios = ['$5','$7','$10']
MateriaPrima = ['Harina','Agua','Levadura']

listas = memDinamica(Panaderia)
listas.imprimirLista()
listas.agregarelementoarray('muffin')
listas.imprimirLista()
listas.agregarelementoarray('Pan blanco')
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.eliminarElemento('Chilindrina')
listas.imprimirLista()


listas1 = memDinamica(Precios)
listas1.imprimirLista()
listas1.agregarelementoarray('$12')
listas1.imprimirLista()

listas2 = memDinamica(MateriaPrima)
listas2.imprimirLista()
listas2.agregarelementoarray('Mano de Obra')
listas2.imprimirLista()
listas2.ordenarLista()
listas2.imprimirLista()
listas2.insertarNPosicion(1,'acido')
listas2.imprimirLista()
