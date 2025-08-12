def filtrarNom():
    listadoDeNombres = []
    print("PROGRAMA PARA FILTRAR/ENCONTRAR NOMBRES QUE INICIEN CON UNA VOCAL")
    print("Ingrese 10 nombres (Ana, Oscar, Luis, Miguel):")
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