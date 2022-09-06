from xml.dom import minidom
from xml.etree.ElementTree import (Element, SubElement, Comment, tostring,)
import SuperGlobal as sg

def leer_archivo(ruta):
    doc = minidom.parse(ruta)

    pacientes = doc.getElementsByTagName("paciente")
    
    return pacientes

def formato(elem):
    #da saltos de linea y espaciados a xml
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generar_xml_salida():
    lista_pacientes = sg.lista_pacientes
    el_paciente = lista_pacientes.cabeza

    top = Element('pacientes')

    while el_paciente != None:

        datos = el_paciente.paciente

        if datos.resultado != None:
            paciente = SubElement(top, 'paciente')

            datos_personales = SubElement(paciente, 'datospersonales')

            nombre = SubElement(datos_personales, 'nombre')
            nombre.text = datos.nombre
            edad = SubElement(datos_personales, 'edad')
            edad.text = str(datos.edad)

            periodos = SubElement(paciente, 'periodos')
            periodos.text = str(datos.periodos)
            m = SubElement(paciente, 'm')
            m.text = str(datos.m_rejilla)
            resultado = SubElement(paciente, 'resultado')
            resultado.text = str(datos.resultado)

            if datos.n != None:
                n = SubElement(resultado, 'n')
                n.text = str(datos.n)

            if datos.n_1 != None:    
                n_1 = SubElement(resultado, 'n1')
                n_1.text = str(datos.n_1)

        el_paciente = el_paciente.siguiente

    datos_escritura = formato(top)
    archivo = open("resultados.xml", "w")
    archivo.write(datos_escritura)
    archivo.close()
    
    print("\nSe creó archivo con los resultados, encuentralo en \033[1mresultados.xml \033[0m\n")
