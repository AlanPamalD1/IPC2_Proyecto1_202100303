from xml.dom import minidom

#ruta = input("Ingrese la ruta del documento\n")
ruta = "E:\Mis Documents\Programacion\Python\IPC2\LAB\proyecto 1\Tarea1.xml"
doc = minidom.parse(ruta)

pacientes = doc.getElementsByTagName("paciente")

for paciente in pacientes:
    
    nombre = paciente.getElementsByTagName("nombre")[0]
    edad = paciente.getElementsByTagName("edad")[0]
    periodos = paciente.getElementsByTagName("periodos")[0]
    m = paciente.getElementsByTagName("m")[0]
    celdas = paciente.getElementsByTagName("celda")

    print("Nombre: %s " % nombre.firstChild.data)
    print("Edad: %s " % edad.firstChild.data)
    print("Periodos: %s" % periodos.firstChild.data)
    print("m: %s" % m.firstChild.data)

    for celda in celdas:
        print("Celda f: %s, c: %s" %(celda.getAttribute("f"),celda.getAttribute("c")))

    print(" ")    