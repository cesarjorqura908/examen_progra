
#variables principales
depas = [] #almacena en una matriz de 10x4 los depas vendidos y disponibles
clientes = [] #almacena los numeros de depas comprados y el rut asociado lista de 2 columnas y n filas
ganancias = 0 #acumulador de las ventas de depas
a = 0
b = 0
c = 0
d = 0

def crear_depas():
    global depas
    for i in range(10):
        depas.append([0, 0, 0, 0])
    return

def mostrar_depas():
    aux = 10
    print("       A  B  C  D")
    for i in range(10):
        print(f"{aux}:   {depas[i]}")
        aux -= 1

def mostrar_precios():
    print("A = 3.800UF")
    print("B = 3.000UF")
    print("C = 2.800UF")
    print("D = 3.500UF")

def comprar_depa():

    global depas, ganancias, clientes, a, b, c, d#sentencia global para poder usar variables que esten fuera de la funcion
    piso = int(input("Ingrese el piso en el que desea comprar un departamento"))
    mostrar_precios()
    letra = input("ingrese el tipo de departamento que desea comprar, selecionando una letra del menue")
    if letra == "a":
        aux = 0
    elif letra == "b":
        aux = 1
    elif letra == "c":
        aux = 2
    elif letra == "d":
        aux = 3

    if piso < 1 or piso > 10:
        print("Número de piso invalido.")
        return
    if letra != "a" and letra != "b" and letra != "c" and letra != "d":
        print("tipo de departamento invalido ")
        return

    for i in range(10):
        for j in range(4):
            if depas[piso-10][aux] == "X":
                print("departamento vendido lo sentimos seleccione uno nuevo")
                return
    depas[piso - 10][aux] = "X"

    if aux == 0:
        a += 1
    elif aux == 1:
        b += 1
    elif aux == 2:
        c += 1
    elif aux == 3:
        d += 1

    run = int(input("Ingrese el RUN de la persona que ocupará el asiento: "))
    clientes.append([run])
    print("Departamento comprado exitosamente!.")
    return

def mostrar_clientes():
    global clientes
    if(clientes):
        clientes.sort()
        for i in range(len(clientes)):
            print(f"cliente{i+1}:")
            print(clientes[i])

def ganancias():
    global a, b, c, d
    print(f"tipo A 3800 UF      {a}     {a*3800} uf")
    print(f"tipo B 3000 UF      {b}     {b * 3000} uf")
    print(f"tipo C 2800 UF      {c}     {c * 2800} uf")
    print(f"tipo D 3500 UF      {d}     {d * 3500} uf")
    ganancias = ((a*3800)+(b*3000)+(c*2800)+(d*3500))
    print(f"TOTAL     {a+b+c+d}      {ganancias} uf")

def ejecutar_programa():
    salir = 1
    while(salir):
        print("BIENVENIDO AL ASISTENTE DE COMPRA DE DEPARTAMENTOS")
        print("Seleccione una opcion del menu pulsando el numero de la opcion")
        print("1)Comprar departamento")
        print("2)departamentos disponibles")
        print("3)Listado de clientes ")
        print("4)Ganancias Totales")
        print("5)Salir")
        opc = int(input("ingrese su opcion"))
        if opc == 1:
            mostrar_depas()
            comprar_depa()
        elif opc == 2:
            mostrar_depas()
        elif opc == 3:
            mostrar_clientes()
        elif opc == 4:
            ganancias()
        elif opc == 5:
            print("Cesar Jorquera 10/07/2023")
            exit()
        else:
            print("ingrese una opcion valida")
            ejecutar_programa()


#programa principal
crear_depas()
ejecutar_programa()

