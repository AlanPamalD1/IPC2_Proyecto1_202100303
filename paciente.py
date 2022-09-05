class Paciente:
    
    def __init__(self, nombre , edad , periodos , m_rejilla ):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m_rejilla = m_rejilla
        self.resultado = None
        self.n = None
        self.n_1 = None
    
    def imprimir(self):
        text = "Nombre: %s, Edad: %s, Periodos: %s, Tamaño de rejillas: %s" %(self.nombre, self.edad, self.periodos, self.m_rejilla)
        print(text)