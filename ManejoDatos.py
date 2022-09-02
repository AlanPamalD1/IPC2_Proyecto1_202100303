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

def generar_rejilla_nuevo_periodo(rejilla):
    
    rejilla_temp = rejilla

    tmpV_a = rejilla.raiz
    tmpV_b = m_b.raiz
    validacion = True

    #Movilizar por las filas y columnas de la matriz
    while tmpV_a != None:
        tmpH_a = tmpV_a
        tmpH_b = tmpV_b
        while tmpH_a != None:
            validacion = comparar_datos_celdas(tmpH_a,tmpH_b)
            if  not validacion :
                return False
            tmpH_a = tmpH_a.derecha
            tmpH_b = tmpH_b.derecha
        
        tmpV_a = tmpV_a.abajo
        tmpV_b = tmpV_b.abajo
    
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
    
def comparar_datos_celdas(celda_a, celda_b):
    #Si es distinto regresa False, de lo contrario
    if (celda_a.dato != celda_b.dato):
        return False
    return True

def comparar_matrices(m_a, m_b):
    if (m_a.filas() == m_b.filas() and m_a.columnas() == m_b.columnas()):
        #Matrices del mismo tamaño, se procede a comparar cada celda

        tmpV_a = m_a.raiz
        tmpV_b = m_b.raiz
        validacion = True

        #Movilizar por las filas y columnas de la matriz
        while tmpV_a != None:
            tmpH_a = tmpV_a
            tmpH_b = tmpV_b
            while tmpH_a != None:
                validacion = comparar_datos_celdas(tmpH_a,tmpH_b)
                if  not validacion :
                    return False
                tmpH_a = tmpH_a.derecha
                tmpH_b = tmpH_b.derecha
            
            tmpV_a = tmpV_a.abajo
            tmpV_b = tmpV_b.abajo

        return True    
    else:
        #Matrices no son del mismo tamaño, por lo cual no son iguales
        return False

def verificar_repeticion_rejillas(i):
    pass

def iniciarSimulacion(n_paciente):
    
    
    el_paciente = sg.lista_pacientes.cabeza
    contador = 1
    

    while contador < n_paciente:
        contador += 1
        el_paciente = el_paciente.siguiente
    
    if el_paciente != None:
        datos_paciente = el_paciente.paciente
        print("Se inicia simulacion con el paciente No. %s, %s"%(contador, datos_paciente.nombre))
        
        
        listado_rejillas = el_paciente.lista_rejillas
        rejilla = listado_rejillas.cabeza.rejilla

        contador_periodos = 0
        num_rejilla_repetida = None
      
        
        while contador_periodos <= el_paciente.paciente.periodos and num_rejilla_repetida != -1:

            rejilla.recorrerMatriz()

            rejilla_nueva = generar_rejilla_nuevo_periodo(rejilla)
            listado_rejillas.add_nodo_final(rejilla_nueva)

            for i in range (listado_rejillas.tamano()-1):
                num_rejilla_repetida = verificar_repeticion_rejillas(i)
            
                if (num_rejilla_repetida != -1):
                    datos_paciente.resultado = "mortal"
                    break
        
            rejilla = rejilla.siguiente
            contador_periodos += 1
        
    else:
        print("Número de paciente no válido")

    

    

