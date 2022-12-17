numero = int(input("Cuántos números va a ingresar?: "))

list = []
for n in range(numero):
    a = int(input("Ingrese un número: "))
    list.append(a)
print(sorted(list)[-2])