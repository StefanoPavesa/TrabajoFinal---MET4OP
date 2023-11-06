numero = int(input("Ingrese su número: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("El numero es primo")
else:
    print("El numero no es primo")
