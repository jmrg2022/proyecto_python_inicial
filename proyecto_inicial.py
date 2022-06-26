# Proyecto Python

from ast import Pass
import csv
import datetime


def read_csv_usuario(usringresado, passingresado): 

    csvfile = open('usuarios.csv')
    
    usuarios = list(csv.DictReader(csvfile))

    BandUs=0

    for usuario in usuarios:
        
        if usringresado == usuario['usuario']:
            
            if passingresado == usuario['clave']:

                BandUs=1

    csvfile.close()

    return BandUs

def read_csv_usuario_rptasecreta(usringresado, rptasecreta): 

    csvfile = open('usuarios.csv')
    
    usuarios = list(csv.DictReader(csvfile))

    BandUsRpta=0

    for usuario in usuarios:
        
        if usringresado == usuario['usuario']:
            
            if rptasecreta == usuario['rptasecreta']:

                BandUsRpta=1

    csvfile.close()

    return BandUsRpta

def modificar_datos_usuarios(useringresado, nuevaclave):

    csvfile = open('usuarios.csv')
    
    usuarios = list(csv.DictReader(csvfile))

    fila=0

    for filas in usuarios:
        if filas['usuario'] == useringresado:            
            usuarios[fila]['clave'] = nuevaclave
        fila=fila+1

    csvfile.close()

    csvfile = open('usuarios.csv', 'w', newline='')

    header = ['usuario', 'apellidoynombre', 'clave', 'rptasecreta']

    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()

    writer.writerows(usuarios)

    csvfile.close()

def read_csv_movimientoscaja(fechainicial,fechafinal,tipomovimiento):

    csvfile = open('movimientoscaja.csv')
    
    movimientoscaja = list(csv.DictReader(csvfile))

    listadotipocomprobantes = []
 
    for movcaja in movimientoscaja:

        if movcaja['Fecha'] > fechainicial and movcaja ['Fecha'] < fechafinal and tipomovimiento == movcaja['Flujo']:

            listadotipocomprobantes.append(movcaja['TipoComprobante'])
            #tipocomprobante=movcaja['TipoComprobante']
            #sumatipocomprobante = sumatipocomprobante + float(movcaja['Importe'])

    csvfile.close()

    listadotipocomprobantesset = set(listadotipocomprobantes)    
    newlistadotipocomprobantes = list(listadotipocomprobantesset)    
    listadotipocomprobantes = list(newlistadotipocomprobantes)
    listadotipocomprobantes.sort()

    for tipocomprob in listadotipocomprobantes:

        sumatipocomprobante = 0
        cantcomprobante = 0

        for movcaja in movimientoscaja:

            if tipocomprob == movcaja['TipoComprobante']:
                
                sumatipocomprobante = sumatipocomprobante + float(movcaja['Importe'])
                cantcomprobante = cantcomprobante + 1

        sumatipocomprobante = round(sumatipocomprobante,2)
        print(tipocomprob,'Cantidad:',cantcomprobante,'Suma:',sumatipocomprobante)

if __name__ == '__main__':

    print("Bienvenidos a mi Proyecto Inicial Python")
    
    useringresado = str(input('Ingrese usuario:'))
    
    passingresado = str(input('Ingrese contraseña:'))
    
    BandUs=read_csv_usuario(useringresado, passingresado)
    
    if BandUs == 1:

        print("Seleccione las Opciones a Listar")

        fechainicial = str(input('Ingrese Fecha Inicial entre 01Ene2022 a 30Abr2022 en formato (dd/mm/aaaa):'))
        fechafinal = str(input('Ingrese Fecha Final entre 01Ene2022 a 30Abr2022 en formato (dd/mm/aaaa):'))
        tipomovimiento = str(input('Ingrese Movimiento (INGRESOS/EGRESOS):'))

        print("Resultado de su Selección:")

        read_csv_movimientoscaja(fechainicial,fechafinal,tipomovimiento)

    else:
        print('Usuario o contraseña incorrecta')
        
        pregpass = str(input('¿Desea restablecer su contraseña (S/N)?'))

        if pregpass == "S":
            
            useringresado = str(input('Ingrese usuario:'))
    
            rptasecreta = str(input('Ingrese Respuesta Secreta:'))

            BandUsRpta=read_csv_usuario_rptasecreta(useringresado, rptasecreta)

            if BandUsRpta == 1:

                clavenueva = str(input('Ingrese nueva contraseña:'))
    
                confclavenueva = str(input('Reconfirme nueva contraseña:'))

                if clavenueva == confclavenueva:

                    modificar_datos_usuarios(useringresado, clavenueva)

                    print('Su contraseña fue reestrablecida con la última que ingresó...')
                
                else:

                    print('Nueva contraseña y confirmación de nueva contraseña no coinciden !!!')

            else:
                
                print('Incorrecto')
