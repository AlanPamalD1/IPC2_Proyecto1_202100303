from paciente import Paciente
from MatrizOrtogonal import Matriz
from ListaRejillas import ListaDoble as l_rej
import SuperGlobal as sg

#funciones simples
def suma_celdas_valor(celda, valor):
    if celda != None and celda.dato == valor:
        return 1
    else:
        return 0

def get_n_celdas_valor(rejilla, valor):

    contador = 0
    tmpV = rejilla.raiz
    
    while tmpV != None:
        tmpH = tmpV
        
        #nos vamos a la derecha 
        while tmpH != None:
            if (tmpH.dato == valor):
                contador +=1
            tmpH = tmpH.derecha

        #se termino una fila
        tmpV = tmpV.abajo
    
    return contador


#manejo rejillas (matrices ortogonales)
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

def verificar_repeticion_rejillas(listado_rejillas, rejilla):
    rejilla_temp = listado_rejillas.cabeza

    contador_busqueda = 0

    while rejilla_temp.siguiente != None:

        comparacion = comparar_matrices(rejilla_temp.rejilla, rejilla)


        if comparacion and rejilla_temp.rejilla != rejilla:
            return contador_busqueda
        else:
            contador_busqueda += 1
            rejilla_temp = rejilla_temp.siguiente

    return (-1)

def generar_rejilla(m, celdas):

    matriz = Matriz()

    for i in range(1,m+1):
        for j in range (1,m+1):
            estado = sg.VALOR_SANO

            for celda in celdas:
                fila = int(celda.getAttribute("f"))
                columna = int(celda.getAttribute("c"))

                if(fila == i and columna == j):
                    estado = sg.VALOR_CONTAGIADO
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
            estado_celda = tmpH.dato
            contador_celdas_contagiadas = 0

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

            contador_celdas_contagiadas += suma_celdas_valor(celda_1, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_2, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_3, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_4, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_5, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_6, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_7, sg.VALOR_CONTAGIADO)
            contador_celdas_contagiadas += suma_celdas_valor(celda_8, sg.VALOR_CONTAGIADO)

            celda_valida = True

            #Verificar que no sea la primera fila o columna
            if tmpH_temp.posHorizontal == 0:
                celda_valida = False
            if tmpH_temp.posVertical == 0:
                celda_valida = False

            
            if estado_celda == sg.VALOR_SANO :
                if contador_celdas_contagiadas >= sg.N_CELDAS_CONTAGIAR_SANA and celda_valida:
                    #print("Celda en fila %s columna %s se contagio" %(tmpH.posHorizontal, tmpH.posVertical))
                    tmpH_temp.dato = sg.VALOR_CONTAGIADO
                elif contador_celdas_contagiadas < sg.N_CELDAS_CONTAGIAR_SANA and celda_valida:
                    tmpH_temp.dato = sg.VALOR_SANO

            elif estado_celda == sg.VALOR_CONTAGIADO:
                if contador_celdas_contagiadas >= sg.N_CELDAS_CONTAGIAR_CONTAGIADA and celda_valida:
                    #print("Celda en fila %s columna %s se contagio" %(tmpH.posHorizontal, tmpH.posVertical))
                    tmpH_temp.dato = sg.VALOR_CONTAGIADO
                elif contador_celdas_contagiadas < sg.N_CELDAS_CONTAGIAR_CONTAGIADA and celda_valida:
                    tmpH_temp.dato = sg.VALOR_SANO

            #siguiente columna
            tmpH = tmpH.derecha
            tmpH_temp = tmpH_temp.derecha

        #se termino una fila
        tmpV = tmpV.abajo
        tmpV_temp = tmpV_temp.abajo
    
    return rejilla_temp

def verificar_repeticion_patron(patron_repetido, num_periodos, datos_paciente):
    n_patron = abs(patron_repetido - num_periodos)

    if patron_repetido > 0 :

        print("\nSe encontró una repetición del periodo %s con el periodo %s" %(patron_repetido, num_periodos))
        print("Repetición cada %s periodos desde el periodo %s" %(n_patron, patron_repetido))

        #caso grave si n_patron
        #mortal si n_patron = 1
        if n_patron == 1:
            datos_paciente.resultado = "mortal"
        else:
            datos_paciente.resultado = "grave"
        
        datos_paciente.n = num_periodos
        datos_paciente.n_1 = n_patron
        
        return True
    elif patron_repetido == 0 :
        print("\nSe encontró una repetición del periodo %s con el periodo inicial" %(num_periodos))
        print("Repetición cada %s periodos desde el periodo %s" %(n_patron, patron_repetido))

        #caso grave si n_patron
        #mortal si n_patron = 1
        if n_patron == 1:
            datos_paciente.resultado = "mortal"
            
        else:
            datos_paciente.resultado = "grave"
        
        datos_paciente.n = num_periodos
        datos_paciente.n_1 = n_patron
        return True
    else:
        #enfermedad leve, no repitencia de periodos
        datos_paciente.resultado = "leve"
        datos_paciente.n = None
        datos_paciente.n_1 = None
        return False


#manejo pacientes
def get_paciente_n (n):
    el_paciente = sg.lista_pacientes.cabeza
    contador = 1
    while contador < n:
        contador += 1
        el_paciente = el_paciente.siguiente
        if el_paciente == None:
            return None
        
    return el_paciente

def listar_pacientes_entrada (datos):

    for paciente in datos:
        rejilla_valida = True
        lista_rejilla = l_rej()
        matriz = Matriz()

        nombre = paciente.getElementsByTagName("nombre")[0].firstChild.data
        edad = paciente.getElementsByTagName("edad")[0].firstChild.data
        periodos = int(paciente.getElementsByTagName("periodos")[0].firstChild.data)
        m = int(paciente.getElementsByTagName("m")[0].firstChild.data)
        celdas = paciente.getElementsByTagName("celda")

        if m % sg.MULTIPLICIDAD_REJILLA != 0 :
            rejilla_valida = False
            print("No se pudo ingresar al paciente %s con una rejilla de tamaño %s x %s, el tamaño debe ser cuadrado y con multiplicidad %s" %(nombre, m, m, sg.MULTIPLICIDAD_REJILLA))
        elif m > sg.LIMITE_REJILLA:
            rejilla_valida = False
            print("No se pudo ingresar al paciente %s con una rejilla de tamaño %s x %s, el limite permitido es %s x %s." %(nombre, m, m, sg.LIMITE_REJILLA,sg.LIMITE_REJILLA))
        if periodos > sg.LIMITE_PERIODOS :
            print("No se pudo ingresar al paciente %s con un número de periodos de %s, el limite permitido es %s periodos." %(nombre, periodos, sg.LIMITE_PERIODOS))
            rejilla_valida = False

        if rejilla_valida : 
            datos_paciente = Paciente(nombre, edad, periodos, m)

            matriz = generar_rejilla(m, celdas)
            lista_rejilla.add_nodo_final(matriz)

            sg.lista_pacientes.add_nodo_final(datos_paciente, lista_rejilla)


#impresiones
def impimir_datos_periodo(num_periodos, rejilla):
    print("\n*********************************************")
    print("Periodo No. "+ str(num_periodos))
    print("Número de celdas contagiadas: %s" %(get_n_celdas_valor(rejilla, sg.VALOR_CONTAGIADO)))
    print("Número de celdas sanas: %s" %(get_n_celdas_valor(rejilla, sg.VALOR_SANO)))

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


#simulaciones
def simulacion_automática(n_paciente):
    
    el_paciente = get_paciente_n(n_paciente)
    
    if el_paciente != None :
        datos_paciente = el_paciente.paciente
        listado_rejillas = el_paciente.lista_rejillas

        num_periodos = listado_rejillas.tamano()-1

        print("Se inicia simulación automática con el paciente %s con %s periodos" %(datos_paciente.nombre, datos_paciente.periodos))
        if num_periodos >0:
            print("Retomando simulación en periodo No %s" %(num_periodos))

        while num_periodos <= datos_paciente.periodos:
            
            rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)
            num_periodos = listado_rejillas.tamano()-1

            impimir_datos_periodo(num_periodos, rejilla)

            rejilla_repetida = verificar_repeticion_rejillas(listado_rejillas, rejilla)
            patron_repetido = verificar_repeticion_patron(rejilla_repetida, num_periodos, datos_paciente)

            if patron_repetido:
                break
            else:

                if num_periodos == el_paciente.paciente.periodos:
                    print("\nSe alcanzó el límite de peridos disponibles\n")
                    break
                else:
                    rejilla_nueva = generar_rejilla_nuevo_periodo(rejilla)
                    listado_rejillas.add_nodo_final(rejilla_nueva)
                
        rejilla.recorrerMatriz()

        print("\nEl paciente tiene un caso %s" %(datos_paciente.resultado))                            
        print("\nTerminando simulación automática\n")           
                
                    
    else:
        print("Número de paciente no válido")

def simulacion_manual(n_paciente):
    
    el_paciente = get_paciente_n(n_paciente)
    
    if el_paciente != None :
        datos_paciente = el_paciente.paciente
        listado_rejillas = el_paciente.lista_rejillas

        num_periodos = listado_rejillas.tamano()-1
        if num_periodos >0:
            print("Retomando simulación en periodo No %s" %(num_periodos))

        print("Se inicia simulacion manual con el paciente %s con %s periodos" %(datos_paciente.nombre, datos_paciente.periodos))

        while num_periodos <= datos_paciente.periodos:
            
            rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)
            num_periodos = listado_rejillas.tamano()-1

            impimir_datos_periodo(num_periodos, rejilla)
            rejilla.recorrerMatriz()

            rejilla_repetida = verificar_repeticion_rejillas(listado_rejillas, rejilla)
            patron_repetido = verificar_repeticion_patron(rejilla_repetida, num_periodos, datos_paciente)
            
            
            if patron_repetido:
                break
            else:
                if num_periodos == el_paciente.paciente.periodos:
                    print("\nSe alcanzó el límite de peridos disponibles\n")
                    break
                else:
                    rejilla_nueva = generar_rejilla_nuevo_periodo(rejilla)
                    listado_rejillas.add_nodo_final(rejilla_nueva)

                    input_siguiente = input("\n¿Desea ver el siguiente periodo?\nS = si\nN = no\nA = periodo automático\n")
                    if input_siguiente == "N" or input_siguiente == "n":
                        break
                    elif input_siguiente == "A" or input_siguiente == "a":
                        simulacion_automática(n_paciente)
                        break
                

        print("\nEl paciente tiene un caso %s" %(datos_paciente.resultado))                            
        print("\nTerminando simulación\n")           

    else:
        print("Número de paciente no válido")

def simulacion_masiva(n_paciente):
    el_paciente = get_paciente_n(n_paciente)
    
    if el_paciente != None :
        datos_paciente = el_paciente.paciente
        listado_rejillas = el_paciente.lista_rejillas

        num_periodos = listado_rejillas.tamano()-1

        print("Se inicia simulación masiva del paciente %s." %(datos_paciente.nombre))
        if num_periodos >0:
            print("Retomando simulación en periodo No %s" %(num_periodos))

        while num_periodos <= sg.LIMITE_PERIODOS:
            
            rejilla = get_ultimo_rejilla_ultimo_periodo(listado_rejillas)
            num_periodos = listado_rejillas.tamano()-1

            impimir_datos_periodo(num_periodos, rejilla)

            rejilla_repetida = verificar_repeticion_rejillas(listado_rejillas, rejilla)
            patron_repetido = verificar_repeticion_patron(rejilla_repetida, num_periodos, datos_paciente)

            if patron_repetido:
                break
            else:

                if num_periodos == el_paciente.paciente.periodos:
                    print("\nSe alcanzó el límite de peridos disponibles\n")
                    break
                else:
                    rejilla_nueva = generar_rejilla_nuevo_periodo(rejilla)
                    listado_rejillas.add_nodo_final(rejilla_nueva)
        
        rejilla.recorrerMatriz()

        print("\nEl paciente tiene un caso %s" %(datos_paciente.resultado))                            
        print("\nTerminando simulación masiva\n")           
                    
    else:
        print("Número de paciente no válido")   

