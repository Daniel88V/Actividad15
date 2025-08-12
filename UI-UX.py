def filtrarNom():
    listadoDeNombres = []
    print("PROGRAMA PARA FILTRAR/ENCONTRAR NOMBRES QUE INICIEN CON UNA VOCAL")
    print("Ingrese 10 nombres (ejemplo: Ana, Oscar, Luis, Miguel):")
    for i in range(10):
        nombre = input(f"Nombre #{i + 1}: ").upper()
        while nombre == "":
            nombre = input(f"Nombre #{i + 1}: ").strip()
            if nombre == "":
                print("Error. Este campo es requerido, por favor ingrese un nombre")
        listadoDeNombres.append(nombre)
    print("Nombres que empiezan con una vocal: ")
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for nombre in listadoDeNombres:
        if len(nombre) > 0:
            primerLetra = nombre[0]
            if primerLetra in vocales:
                print(nombre)
def promedio():
    Numeros = []
    print("PROGRAMA PARA CALCULAR PROMEDIO")
    print("Ingrese numeros positivos, si desea continuar ingrese un numero negativo")
    while True:
        Ingreso = input("Ingresa número: ")
        numero = float(Ingreso)
        if numero < 0:
            print("Valor incorrecto, intenta de nuevo.")
        if numero > 0:
            break
    Numeros.append(numero)
    if len(Numeros) > 0:
        suma = sum(Numeros)
        cantidad = len(Numeros)
        promedio = suma / cantidad
        """
        for num in Numeros:
            suma += num
        cantidad = len(Numeros)
        promedio = suma/cantidad
        """
        print(f"La suma de los números positivos es: {suma}")
        print("La cantidad de numeros es: ", cantidad)
        print(f"El promedio de los números positivos es: {promedio:.2f}")
    else:
        print("No se ingresó ningún número positivo para calcular el promedio.")
def convertir_temperatura():
    while True:
        print("Escoja la conversión que desea efectuar")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Volver al Menú Principal")
        grados_opcion = input()
        match grados_opcion:
            case "1":
                while True:
                    print("Ingrese los grados Celsius: ")
                    celsius = float(input())
                    if celsius > 0:
                        fahrenheit = (celsius * 9/5) + 32
                        print(f"{celsius:.2f}°C a Fahrenheit es: {fahrenheit:.2f}°F")
                    elif celsius < 0:
                        print("Error, por favor ingrese los grados en números")
                    else:
                        break
            case "2":
                while True:
                    print("Ingrese los grados Fahrenheit: ")
                    fahrenheit = float(input())
                    if fahrenheit > 0:
                        celsius = (fahrenheit - 32) * 5/9
                        print(f"{fahrenheit:.2f}°F a Celsius es: {celsius:.2f}°C")
                    elif fahrenheit < 0:
                        print("Error, por favor ingresar los grados en números")
                    else:
                        break
            case "3":
                print("Volviendo al menú principal...")
                break
            case _:
                print("Opción no disponible")
def calcular_area():
    print(" --- Calcular Área ---")
    while True:
        print("Cuadrado - 1")
        print("Círculo - 2")
        print("Triángulo - 3")
        print("Volver al Menú Principal - 4")
        eleccion = input("Seleccione una opción: ")
        match eleccion:
            case "1":
                while True:
                    x = float(input("Ingrese el valor de un lado del cuadrado(8, 7.5, 23): "))
                    if x > 0:
                        area = x * x
                        print(f"El área del cuadrado es: {area:.2f}u^2")
                    elif x < 0:
                        print("Por favor ingresa un número")
                    else:
                        break
            case "2":
                while True:
                    z = float(input("Ingrese el valor del radio: "))
                    if z > 0:
                        area = z * z * 3.1416
                        print(f"El área del círculo es: {area:.2f}u^2")
                    elif z < 0:
                        print("Por favor ingresa un número positivo")
                    else:
                        break
            case "3":
                while True:
                    y = float(input("Ingrese el valor de la altura: "))
                    j = float(input("Ingrese el valor de la base: "))
                    if y > 0 and j > 0:
                        area = (y * j) / 2
                        print(f"El área del triángulo es: {area:.2f}u^2")
                    elif y < 0 or j < 0:
                        print("Error. Hay un valor que invalida la ecuación, por favor trate de nuevo")
                    else:
                        break
            case "4":
                print("Volviendo al menú principal...")
                break
            case _:
                print("Opción no disponible")
def menu():
    print("======MENÚ PRINCIPAL======")
    print("1. Filtrar Nombres Cuya Inicial Sea Una Vocal.")
    print("2. Calcular Promedio.")
    print("3. Menú Conversión de Temperatura.")
    print("4. Menú Calcular Area.")
    print("5. Salir.")
    opcion = input("Selecione una de las opcines(1-5): ")
    while True:
        match opcion:
            case "1":
                print("¿Desea continuar hacia el programa o volver al menú principal?")
                print("Si/No: ")
                afirmacion = input().upper()
                if afirmacion == "SI":
                    filtrarNom()
                    print("¿Desea repetir la funcion?")
                    print("Si = 1 | No = 2")
                    seleccion = int(input())
                    if seleccion == 1:
                        filtrarNom()
                    elif seleccion == 2:
                        break
                    else:
                        print("Opcion no valida, por favor seleccione Si(1) o No(2)")
                elif afirmacion == "NO":
                    break
                else:
                    print("Opcion no valida, por favor escriba Si o No")
            case "2":
                print("¿Desea continuar hacia el programa o volver al menú principal?")
                print("Si/No: ")
                afirmacion = input().upper()
                if afirmacion == "SI":
                    promedio()
                    print("¿Desea repetir la funcion?")
                    print("Si = 1 | No = 2")
                    seleccion = int(input())
                    if seleccion == 1:
                        filtrarNom()
                    elif seleccion == 2:
                        break
                    else:
                        print("Opcion no valida, por favor seleccione Si(1) o No(2)")
            case "3":
                print("Bienvenido al menú de conversion de temperatura.")
                convertir_temperatura()
                print("¿Desea repetir la funcion?")
                print("Si = 1 | No = 2")
                seleccion = int(input())
                if seleccion == 1:
                    filtrarNom()
                elif seleccion == 2:
                    break
                else:
                    print("Opcion no valida, por favor seleccione Si(1) o No(2)")
