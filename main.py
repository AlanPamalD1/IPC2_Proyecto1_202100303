
import ManejoDatos as md
import ManejoArchivos as ma
import SuperGlobal as sg

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
                
                md.iniciar_simulacion_manual(num_paciente)

            case "3":
                print("")
                
            case "4":
                programa_en_curso = False
                print("Saliendo del programa ...")
            case _:
                print("Opción no válida")


