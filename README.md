# Proyecto 1
## Laboratorio Introducción a la Programación y Computación 2

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Datos estudiante

| Dato |  |
| ------ | ------ |
| Nombre | Alan Rodrigo Pamal de León |
| Carné | 202100303 |

## Auxiliar

| Dato |  |
| ------ | ------ |
| Nombre | Viany Juárez |
| Carné | 3001620730101 |

## Lenguajes utilizados

- Python
- Grahpvix
- os


## Librerias utilizadas
- minidoom
- ElementTree

## Descripción programa

El programa consta de un simulador de la infección de celulas del cuerpo humano segun patrones a través del uso de rejillas cuadradas con tejido del paciente, las cuales en cada celda contiene el estado de esta, siendo 1 si es contagiada, o 0 si es sana.

Las células contagiadas cuentan con un comportamiento periodico, donde si una célula contagiada esta continua a 2 o más células esta seguira contagiada, de lo contrario se sanara. En caso de que la célula este sana, si está continua a 3 o más contagiadas se contagiara, caso contrario seguira sana.


## Funcionamiento

Los datos del paciente se cargan con un archivo en formato .xml, donde lleva datos del paciente como nombre y edad, el número de periodos que se analizaran en la simulación, el tamaño de la rejilla y las posición de las celdas contagiadas.

Estos datos se guardan para poder hacer la simulación, las cuales pueden ser manuales donde gráficara cada periodo según indique el usuarió, automático donde generara todos los periodos y gráficara el último, y masiva donde realizara una simulación con 10,000 periodos para encontrar alguna repitencia.

Despúes de esto el usuario podrá generar un archivo en formato xml con los resultados encontrados.

### Formato entrada xml
```sh
<pacientes>
    <paciente>
        <datospersonales>
            <nombre>$nombre</nombre>
            <edad>$edad</edad>
        </datospersonales>
        <periodos>5</periodos>
        <m>10</m>
        <rejilla>
            <celda f="1" c="1"/>
            <celda f="1" c="2"/>
            <celda f="2" c="1"/>
            <celda f="2" c="2"/>
            <celda f="6" c="6"/>
            <celda f="6" c="7"/><celda f="7" c="6"/>
            <celda f="7" c="7"/>
        </rejilla>
    </paciente>
    <paciente>
    ....
    </paciente>
</pacientes>
```

### Formato salida xml
```sh
<pacientes>
    <paciente>
        <datospersonales>
            <nombre>$nombre</nombre>
            <edad>$edad</edad>
        </datospersonales>
        <periodos>5</periodos>
        <m>10</m>
        <resultado>leve</resultado>
    </paciente>
    <paciente>
        <datospersonales>
            <nombre>$nombre2</nombre>
            <edad>$edad2</edad>
        </datospersonales>
        <periodos>5</periodos>
        <m>10</m>
        <resultado>grave</resultado>
            <n>3<n/>
    </paciente>
    <paciente>
        <datospersonales>
            <nombre>$nombre3</nombre>
            <edad>$edad3</edad>
        </datospersonales>
        <periodos>10</periodos>
        <m>10</m>
        <resultado>mortal</resultado>
            <n>1<n/>
            <n1>2<n/>
    </paciente>
</pacientes>
```
### Formato gráfica rejilla
Ejemplo de una rejilla de tamaño 10

![rejilla](https://i.imgur.com/GJLVEWJ.png)
