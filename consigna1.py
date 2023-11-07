numero = int(input("Ingrese su número: "))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("Es primo")
else:
    print("No es primo")
    

numero = float((input("Ingrese un numero para saber si es primo: ")))
nro = int(numero)
numero_primo = (nro/nro == 1) or (nro/nro == nro)
if nro == numero_primo:     
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")
    


