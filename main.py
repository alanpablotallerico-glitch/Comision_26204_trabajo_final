import dataset 
mibase=dataset.connect("sqlite:///datos.db")
basededatos=mibase["productos"]




while True:

    opciones=input(f"A-Agregar\nB-Buscar\nL-Listar\nE-Eliminar\nS-Salir ").upper().strip()

     
    if opciones=="A":
        try:
            agregar_elemento=str(input("Agregue un elemento: ")).capitalize().strip()
        except ValueError:
                print("Ingrese un valor de texto")
        
        try:
            Precio=float(input("ingrese el precio: "))
        except ValueError :
            print("Ingresar un valor numerico")
            continue
        
        categoria=input("Agregue categoria: ").capitalize().strip()
       
        agregar={"nombre" : agregar_elemento , "precio": Precio, "categoria":categoria}

        producto=basededatos.insert(agregar)
        
        
        print(f"Se ha agregado {agregar_elemento} con precio {Precio} y es categoria {categoria}")

        

    elif opciones=="B":
        buscar_elemento=input("Buscar elemento: ").capitalize().strip()
        elemento_buscado=basededatos.find_one(nombre=buscar_elemento)
        if elemento_buscado:
            print(f"El elemento {buscar_elemento} ha sido encontrado")
        else:
            print(f"El elemento {buscar_elemento} no ha sido encontrado")
        ###
        #if buscar_elemento in basededatos:
           # print(f"El elemento {buscar_elemento} se ha encontrado")
        #else:
            #print(f"Elemento {buscar_elemento} no encontrado")
            




    elif opciones=="L":
       for elemento in basededatos:
           print(elemento["nombre"],elemento["precio"],elemento["categoria"])




    elif opciones=="E":
            #try:
                eliminar_elementos=input("Ingrese el elemento a remover: ").capitalize().strip()
                eliminacion_de_elementos=basededatos.delete(nombre=eliminar_elementos)
                if eliminacion_de_elementos:
                    print(f"El elemento {eliminar_elementos} ha sido eliminado")
                else:
                     print("Elemento no encontrado")
                
                #elementos.remove(eliminar_elementos)
                #print(f"El elemento {eliminar_elementos} se ha removido con exito")
            #except SyntaxError:
                #print("Ingresa un elemento con letras")
       


    elif opciones=="S":
        break
