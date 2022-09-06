from ListaPacientes import ListaDoble as l_pac

#lista global de pacientes
lista_pacientes = l_pac()

# Tamaño máximo de la rejilla
LIMITE_REJILLA = 10000

# Cantidad de períodos máxima a evaluar
LIMITE_PERIODOS = 10000

# Multiplicidad necesaria que debe de ser la rejilla
MULTIPLICIDAD_REJILLA = 10

# Valor rejilla contagiada
VALOR_CONTAGIADO = "1"

# Valor rejilla sana
VALOR_SANO = "0"

#Numero de celdas contagiadas que deben estar contiguas de una contagiada para seguir contagiada
N_CELDAS_CONTAGIAR_CONTAGIADA = 2

#Numero de celdas contagiadas que deben estar contiguas a sana para ser contagiada
N_CELDAS_CONTAGIAR_SANA = 3