def sistema_seguridad():
    clave_correcta = "IMT902"
    intentos = 0
    
    while intentos < 3:
        clave = input("Ingrese la palabra secreta: ")
        
        if clave == clave_correcta:
            nombre = input("Ingrese su nombre: ")
            print("Bienvenido cruk", nombre)
            return
        
        print("Clave incorrecta. Inténtelo nuevamente.")
        intentos += 1
    
    print("Acceso denegado. Se ha registrado un intento de fraude.")

sistema_seguridad()
