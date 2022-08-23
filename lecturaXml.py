from xml.dom import minidom
from paciente import Paciente
from listaDobleEnlazada import ListaDoble
from Estructuras import MatrizOrtogonal 

#ruta = input("Ingrese la ruta del documento\n")
ruta = "E:\Mis Documents\Programacion\Python\IPC2\LAB\proyecto 1\Tarea1.xml"
doc = minidom.parse(ruta)

pacientes = doc.getElementsByTagName("paciente")
#lista_pacientes = []

for paciente in pacientes:

    #lista_doble = ListaDoble()
    matriz = MatrizOrtogonal()
    nombre = paciente.getElementsByTagName("nombre")[0].firstChild.data
    edad = paciente.getElementsByTagName("edad")[0].firstChild.data
    periodos = paciente.getElementsByTagName("periodos")[0].firstChild.data
    m = paciente.getElementsByTagName("m")[0].firstChild.data
    celdas = paciente.getElementsByTagName("celda")

    datos_paciente = Paciente(nombre, edad, periodos, m)
    
    #lista_pacientes.append(paciente)


    for celda in celdas:
        fila = int(celda.getAttribute("f"))
        columna = int(celda.getAttribute("c"))
        #lista_doble.add_nodo_final( fila )
        matriz.insertarDato("1",fila,columna)
        #print("Celda f: %s, c: %s" %(celda.getAttribute("f"),celda.getAttribute("c")))

    
    
    #lista_doble.imprimir_lista()
    datos_paciente.imprimir()
    matriz.recorrerMatriz()
    print(" ")    

