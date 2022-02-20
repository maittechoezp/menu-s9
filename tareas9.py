#Materia: Estructura de datos
#Nombre: Maitte Micaela Choez Pachay
#Menu interactivo: listas y pilas
class menu():
    opciones=["","1","2","3"]
    while True:
        print("* Menú Interactivo *")
        print("escribe una frase y yo te ayudare a saber cuantas letras y vocales tiene")
        print("1. contador de vocales")
        print("2. Contador de letras")
        print("3. Salir")

        opcion=input("elige una opcion: ")
        if not(opcion in opciones):
            print("No selecciono ninguna opcion valida")
            input("pulse para continuar")
            continue
        if opcion=="1":
            vocal = 0
            v_a = 0
            v_e = 0
            v_i = 0
            v_o = 0
            v_u = 0
            frase = input("Escribe una frase y te dire cuantas vocales tiene:")

            for i in frase:
                if i.lower() == "a":
                    print("tiene la vocal a")
                    v_a += 1
                    vocal += 1
                elif i.lower() == "e":
                    print("tiene la vocal e")
                    v_e += 1
                    vocal += 1
                elif i.lower() == "i":
                    print("tiene la vocal i")
                    v_i += 1
                    vocal += 1
                elif i.lower() == "o":
                    print("tiene la vocal o")
                    v_o += 1
                    vocal += 1
                elif i.lower() == "u":
                    print("tiene la vocal u")
                    v_u += 1
                    vocal += 1
            print("La frase ingresada tiene: ", v_a, " vocales a - ", v_e, " vocales e - ", v_i, " vocales i - ",
                  v_o, "vocales 0 - ", v_u, " vocales u.")
            print("La frase tiene ingresada tiene : ", vocal, " vocales. ")

        if opcion=="2":
            frc = (input("Ingresa una frase y te dire cuantas letras tiene: "))
            let = len(frc)
            cont = 0
            contnum = 0
            contpuc = 0
            suma = 0
            for i in range(0, let):
                if (frc[i].isspace()):
                    cont += 1
                elif (frc[i].isdigit()):
                    contnum += 1
                elif (frc[i] in "?¡¿*,.-_'"):
                    contpuc += 1
                suma = cont + contnum + contpuc
            rpta = let - suma
            print("La frase ingresada tiene",rpta,"letras")
            opciones.pop(3)
            print("¡Gracias por usar este menú! ")

        if opcion=="3":
            print("gracias")
            break