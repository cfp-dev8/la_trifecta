"""
Ejercicio N2 La trifecta

Requisitos a cumplir:
Al iniciar se nos debe pedir ingresar un numero entero, si este es
distinto a 0 el programa inicia, de lo contrario finaliza (tambien si se
ingresa otra cosa que no sea un numero entero).

Se debe poder ingresar una Palabra o Frase y contar cuantos
caracteres tiene dicha palabra o frase
Con el valor obtenido en el punto anterior calcular su Factorial, una
vez hecho esto , decirnos si el resultado es par o impar.

Se deben imprimir los resultados por pantalla en cada paso.
Una vez cumplido esto, deberemos volver a pedir el ingreso de un
número y realizar la verificación del punto 1

"""

# Empiezo el programa con un bucle que se repite siempre
while True:
    # Pido al usuario un número entero
    numero = int(input("Ingresá un número entero distinto de 0 (si ingresas otro valor el programa tira error): "))
    #podria usar try except pero todavia no lo vimos en el curso.

    # Si el número es 0, termina el programa
    if numero == 0:
        print("Ingresaste 0. Fin del programa.")
        break

    # Si el número es distinto de 0, sigo el programa
    texto = input("Ingresá una palabra o frase: ")

    # Cuento cuántos caracteres tiene el texto
    cantidad = len(texto)
    print("Cantidad de caracteres:", cantidad)

    # Calculo el factorial de esa cantidad
    factorial = 1
    for i in range(1, cantidad + 1):
        factorial = factorial * i

    print("El factorial de", cantidad, "es:", factorial)

    # Verifico si el factorial es par o impar
    if factorial % 2 == 0:
        print("El factorial es PAR.")
    else:
        print("El factorial es IMPAR.")

    print("------ Proba otra vez ------")
