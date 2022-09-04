from Paciente import Paciente
from MatrizOrtogonal import Matriz
from ListaRejillas import ListaDoble as l_rej
import SuperGlobal as sg


def listar_pacientes_entrada (datos):

    for paciente in datos:
        lista_rejilla = l_rej()
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

    for i in range(1,m+1):
        for j in range (1,m+1):
            estado = "0"

            for celda in celdas:
                fila = int(celda.getAttribute("f"))
                columna = int(celda.getAttribute("c"))

                if(fila == i and columna == j):
                    estado = "1"
                    break
                
            matriz.insertarDato(estado,i,j)

    return matriz

def copiar_rejilla(rejilla):
    
    rejilla_temp = Matriz()

    tmpV = rejilla.raiz
    
    while tmpV != None:
        tmpH = tmpV
        
        #nos vamos a la derecha 
        while tmpH != None:
            fila = tmpH.posVertical
            columna = tmpH.posHorizontal
            dato = rejilla.getCelda(fila,columna)
            rejilla_temp.insertarDato(dato, fila, columna)
            tmpH = tmpH.derecha

        #se termino una fila
        tmpV = tmpV.abajo
    
    return rejilla_temp

def suma_celdas_contagiadas(celda):
    if celda != None and celda.dato == "1":
        return 1
    else:
        return 0

def generar_rejilla_nuevo_periodo (rejilla):
    rejilla_temp = Matriz()
    rejilla_temp = copiar_rejilla(rejilla)
    f = rejilla_temp.filas()-1
    c = rejilla_temp.columnas()-1
    
    tmpV = rejilla.raiz
    tmpV_temp = rejilla_temp.raiz
    
    while tmpV != None:
        tmpH = tmpV
        tmpH_temp = tmpV_temp
        
        #nos vamos a la derecha 
        while tmpH != None:
            contador_celdas_contagiadas = 0
            

            #print("rejilla en posicion [%s, %s] con valor de: %s"%(tmpH.posVertical,tmpH.posHorizontal, tmpH.dato))

            if (tmpH.posVertical == 0 and tmpH.posHorizontal == 0):
                #print("eszquina superior izquierda")
                celda_1 = None
                celda_2 = None
                celda_3 = None
                celda_4 = None
                celda_5 = tmpH.derecha
                celda_6 = None
                celda_7 = tmpH.abajo
                celda_8 = tmpH.derecha.abajo
            
            elif (tmpH.posVertical == 0 and tmpH.posHorizontal >= c):
                #print("eszquina superior derecha")
                celda_1 = None
                celda_2 = None
                celda_3 = None
                celda_4 = tmpH.izquierda
                celda_5 = None
                celda_6 = tmpH.izquierda.abajo
                celda_7 = tmpH.abajo
                celda_8 = None
            
            elif(tmpH.posVertical >= f and tmpH.posHorizontal == 0):
                #print("eszquina inferior izquierda")
                celda_1 = None
                celda_2 = tmpH.arriba
                celda_3 = tmpH.derecha.arriba
                celda_4 = None
                celda_5 = tmpH.derecha
                celda_6 = None
                celda_7 = None
                celda_8 = None
            
            elif(tmpH.posVertical >= f and tmpH.posHorizontal >= c):
               # print("eszquina inferior derecha")
                celda_1 = tmpH.izquierda.arriba
                celda_2 = tmpH.arriba
                celda_3 = None
                celda_4 = tmpH.izquierda
                celda_5 = None
                celda_6 = None
                celda_7 = None
                celda_8 = None
            
            elif (tmpH.posVertical == 0):
                #print("parte superior")
                celda_1 = None
                celda_2 = None
                celda_3 = None
                celda_4 = tmpH.izquierda
                celda_5 = tmpH.derecha
                celda_6 = tmpH.izquierda.abajo
                celda_7 = tmpH.abajo
                celda_8 = tmpH.derecha.abajo
            
            elif (tmpH.posVertical >= f):
                #print("parte inferior")
                celda_1 = tmpH.izquierda.arriba
                celda_2 = tmpH.arriba
                celda_3 = tmpH.derecha.arriba
                celda_4 = tmpH.izquierda
                celda_5 = tmpH.derecha
                celda_6 = None
                celda_7 = None
                celda_8 = None

            elif(tmpH.posHorizontal >= c):
                #print("parte derecha")
                celda_1 = tmpH.izquierda.arriba
                celda_2 = tmpH.arriba
                celda_3 = None
                celda_4 = tmpH.izquierda
                celda_5 = None
                celda_6 = tmpH.izquierda.abajo
                celda_7 = tmpH.abajo
                celda_8 = None
            
            elif(tmpH.posHorizontal == 0):
                #print("parte izquierda")
                celda_1 = None
                celda_2 = tmpH.arriba
                celda_3 = tmpH.derecha.arriba
                celda_4 = None
                celda_5 = tmpH.derecha
                celda_6 = None
                celda_7 = tmpH.abajo
                celda_8 = tmpH.derecha.abajo
           
            else:
                #print("enmedio de rejilla")
                celda_1 = tmpH.izquierda.arriba
                celda_2 = tmpH.arriba
                celda_3 = tmpH.derecha.arriba
                celda_4 = tmpH.izquierda
                celda_5 = tmpH.derecha
                celda_6 = tmpH.izquierda.abajo
                celda_7 = tmpH.abajo
                celda_8 = tmpH.derecha.abajo

            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_1)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_2)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_3)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_4)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_5)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_6)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_7)
            contador_celdas_contagiadas += suma_celdas_contagiadas(celda_8)
            
            
            

            if contador_celdas_contagiadas >= sg.N_CELDAS_CONTAGIADAS:
                #print("Celda en fila %s columna %s se contagio" %(tmpH.posHorizontal, tmpH.posVertical))
                celda_valida = True
                if tmpH_temp.posHorizontal == 0:
                    celda_valida = False
                if tmpH_temp.posVertical == 0:
                    celda_valida = False
                    
                if celda_valida:
                    tmpH_temp.dato = "1"
            
            #siguiente columna
            tmpH = tmpH.derecha
            tmpH_temp = tmpH_temp.derecha

        #se termino una fila
        tmpV = tmpV.abajo
        tmpV_temp = tmpV_temp.abajo
    
    return rejilla_temp

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
    
def comparar_datos_celdas(nodo_celda_a, nodo_celda_b):
    #Si es distinto regresa False, de lo contrario
    if (nodo_celda_a.dato != nodo_celda_b.dato):
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

def get_ultimo_rejilla_ultimo_periodo(lista_rejillas):
    
    rejillas_temp = lista_rejillas.cabeza
    
    while rejillas_temp.siguiente != None:
        rejillas_temp = rejillas_temp.siguiente
    
    return rejillas_temp.rejilla

def verificar_repeticion_rejillas(i):
    pass

def get_paciente_n (n):
    el_paciente = sg.lista_pacientes.cabeza
    contador = 1
    while contador < n:
        contador += 1
        el_paciente = el_paciente.siguiente
        if el_paciente == None:
            return None
        
    return el_paciente

def iniciar_simulacion_manual(n_paciente):
    
    el_paciente = get_paciente_n(n_paciente)
    
    if el_paciente != None :
        datos_paciente = el_paciente.paciente
        listado_rejillas = el_paciente.lista_rejillas

        num_periodos = listado_rejillas.tamano()-1

        #rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)

        print("Se inicia simulacion con el paciente %s con %s periodos" %(datos_paciente.nombre, datos_paciente.periodos))
        
        num_rejilla_repetida = None
        if num_periodos <= el_paciente.paciente.periodos:

            while num_periodos <= datos_paciente.periodos and num_rejilla_repetida != -1:
            
                rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)
                num_periodos = listado_rejillas.tamano()-1

                print("\n*********************************************")
                print("Periodo No. "+ str(num_periodos))
                rejilla.recorrerMatriz()

                rejilla_nueva = generar_rejilla_nuevo_periodo(rejilla)
                print("rejilla nueva generada con id: %s" %(id(rejilla_nueva)))
                listado_rejillas.add_nodo_final(rejilla_nueva)

                #num_rejilla_repetida = verificar_repeticion_rejillas(i)

                """
                if (num_rejilla_repetida != -1):
                    datos_paciente.resultado = "mortal"
                    break
                """
                if num_periodos >= el_paciente.paciente.periodos:
                    print("Se alcanzó el límite de peridos disponibles")
                    break
                
                input_siguiente = input("\n¿Desea ver el siguiente periodo?\nS = si\nN = no\n")
                if input_siguiente == "N" or input_siguiente == "n":
                    break
        else:
            print("Este paciente ya tiene simulación de sus periodos")
            print("Gráficando ultimo periodo simulado ...")
            rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)
            rejilla.recorrerMatriz()
                    
            
            
            
        
    else:
        print("Número de paciente no válido")

    

    

