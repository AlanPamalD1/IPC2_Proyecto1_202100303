from Paciente import Paciente
from MatrizOrtogonal import Matriz
from ListaRejillas import ListaDoble as l_rej
import SuperGlobal as sg

def listar_pacientes_entrada (datos):
    
    lista_rejilla = l_rej()

    for paciente in datos:

        matriz = Matriz()

        nombre = paciente.getElementsByTagName("nombre")[0].firstChild.data
        edad = paciente.getElementsByTagName("edad")[0].firstChild.data
        periodos = int(paciente.getElementsByTagName("periodos")[0].firstChild.data)
        m = int(paciente.getElementsByTagName("m")[0].firstChild.data)
        celdas = paciente.getElementsByTagName("celda")

        datos_paciente = Paciente(nombre, edad, periodos, m)

        matriz = generar_rejilla(m, celdas)
        lista_rejilla.add_nodo_final(matriz)
        sg.lista_pacientes.add_nodo_final(datos_paciente, lista_rejilla)

def generar_rejilla(m, celdas):

    matriz = Matriz()

    for i in range(m):
        for j in range (m):
            estado = "0"

            for celda in celdas:
                fila = int(celda.getAttribute("f"))
                columna = int(celda.getAttribute("c"))

                if(fila == i+1 and columna == j+1):
                    estado = "1"
                    break
                
            matriz.insertarDato(estado,i+1,j+1)

    return matriz

def imprimir_pacientes():
    print("**************************************")
    print("Lista de pacientes:\n")
    el_paciente = sg.lista_pacientes.cabeza
    contador = 1
    while el_paciente != None:
        
        datos_paciente = el_paciente.paciente

        print("Paciente No.%s" %contador)
        datos_paciente.imprimir()
        print("")
        contador += 1
        el_paciente = el_paciente.siguiente
    print("**************************************\n")
    

def iniciarSimulacion(n_paciente):
    
    try:
        el_paciente = sg.lista_pacientes.cabeza
        contador = 1
        paciente_valido = False

        while contador < n_paciente:
            contador += 1
            el_paciente = el_paciente.siguiente
        
        if el_paciente != None:
            paciente_valido = True
        
        if (paciente_valido):
            pass
            print("Se inicia simulacion con el paciente No. %s, %s"%(contador, el_paciente.paciente.nombre))
        else:
            print("Número de paciente no válido")

    except:
        print("Número de paciente no válido")

    

