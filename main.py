
import ManejoDatos as md
import ManejoArchivos as ma

if __name__ == '__main__':
           
    programa_en_curso = True

    print("")
    ruta = "E:\Mis Documents\Programacion\Python\IPC2\LAB\proyecto 1\Tarea1.xml"
    #ruta = input("Ingrese la ruta del documento\n")
    datos = ma.leer_archivo(ruta)
    
    md.listar_pacientes_entrada(datos)

    while programa_en_curso:

        print("**************************************")
        print("1. Ver pacientes")
        print("2. Simulación de paciente")
        print("3. Generar XML resultados")
        print("4. Salir")
        print("**************************************")
        opcion  = input("Ingrese la opción que desea ejecutar\n")

        match opcion:
            case "1":
                print("")
                md.imprimir_pacientes()
            case "2":
                print("")
                md.imprimir_pacientes()

                num_paciente = int(input("Ingresa el número del del paciente que deseas ver la simulación\n"))
                
                opcion = input("\nSeleccione un método de simulación\n1. Manual\n2. Automática\n3. Masiva\n")
                match opcion:
                    case "1":
                        md.simulacion_manual(num_paciente)
                    case "2":
                        md.simulacion_automática(num_paciente)
                    case "3":
                        md.simulacion_masiva(num_paciente)
                    case _:
                        print("Opción no válida")
                
            case "3":
                ma.generar_xml_salida()
                
            case "4":
                programa_en_curso = False
                print("Saliendo del programa ...")
            case _:
                print("Opción no válida")


