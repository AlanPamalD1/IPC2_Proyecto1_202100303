from xml.dom import minidom

def leer_archivo(ruta):
    doc = minidom.parse(ruta)

    pacientes = doc.getElementsByTagName("paciente")
    
    return pacientes

