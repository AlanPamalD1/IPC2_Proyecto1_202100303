class Nodo:
    def __init__(self, paciente, lista_rejillas):
        self.paciente = paciente
        self.lista_rejillas = lista_rejillas
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def add_nodo_final(self, paciente, lista_rejillas):
        nuevo_nodo = Nodo(paciente, lista_rejillas)

        #Si lista esta vacia
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo

        #Si lista no esta vacia
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def add_nodo_inicio(self, paciente, lista_rejillas):
        nuevo_nodo = Nodo(paciente, lista_rejillas)

        #Si lista esta vacia
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo

        #Si lista no esta vacia
        else:
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        print("*** Inicio Lista ***")
        nodo_temporal = Nodo(None)
        nodo_temporal = self.cabeza
        contador = 0
        while nodo_temporal != None:
            contador += 1
            print("Nodo No.%s ,paciente: %s, No. de rejillas: %s " %(str(contador), str(nodo_temporal.paciente), str(len(nodo_temporal.lista_rejillas)) ))
            nodo_temporal = nodo_temporal.siguiente
            
        print("**** Fin Lista *****")
        
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente

        return contador

    def borrarNodo(self, paciente):
        #creamos un nodo temporal
        nodoTemporal = Nodo(None)

        #el temporal empieza en la cabeza
        nodoTemporal = self.cabeza

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.paciente == paciente:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.cabeza:
                    print("Borrando dato en la cabeza")
                    self.cabeza = self.cabeza.siguiente
                    nodoTemporal.siguiente = None
                    self.cabeza.anterior = None
                #Si ese nodo es la cola
                elif nodoTemporal == self.cola:
                    print("Borrando dato en la cola")
                    self.cola = self.cola.anterior
                    nodoTemporal.anterior = None
                    self.cola.siguiente = None
                #Si no es ni la cola ni la cabeza
                else:
                    print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None

            nodoTemporal = nodoTemporal.siguiente