print("Bienvenido A La Validación de Contraseñas")
contraseña = input("Favor ingrese su contraseña: ")

if len(contraseña) < 8:
    print("Contraseña muy corta, debe tener mas de 8 caracteres ")
else:
    minuscula = False
    for minus in contraseña:
        if minus.islower()== True:
            minuscula = True
    if not minuscula:
        print("La contraseña debe contener al menos una letra minuscula")
        
    num = False
    for carac in contraseña:
        if carac.isdigit()== True:
            num = True
    if not num:
        print("La contraseña debe contener al menos un numero")
    else:
        print("Contraseña Valida")