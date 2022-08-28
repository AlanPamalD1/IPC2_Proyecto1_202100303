class Paciente:
    
    def __init__(self, nombre , edad , periodos , m_rejilla ):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.m_rejilla = m_rejilla
    
    """def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.periodos = 0
        self.m_rejila = 0"""

    def getEdad(self):
        return self.edad
    def getNombre(self):
        return self.nombre
    def getPeriodos(self):
        return self.periodos
    def getMRejilla(self):
        return self.m_rejilla
    
    def setEdad(self, edad):
        self.edad = edad
    def setNombre(self, nombre):
        self.nombre = nombre
    def setPeriodos(self, periodos):
        self.periodos = periodos
    def setMRejilla(self, m):
        self.m_rejilla = m
    
    def imprimir(self):
        text = "Nombre: %s, Edad: %s, Periodos: %s, Tamaño de rejillas: %s" %(self.nombre, self.edad, self.periodos, self.m_rejilla)
        print(text)