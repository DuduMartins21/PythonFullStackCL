numero = int(input("digite um numero:"))
for i in range(numero, -1, -1):
    print(i)



numero = int(input("digite um nuero para somar de 1 ate ele:"))
soma = 0
i = 1
while i <= numero:
    soma += i
    i += 1
    print("soma:", soma)



numero = int(input("digte um numero:"))
for i in range(1, 11):
    print(numero, "x", i, "=", numero *i)


numero = int(input("digte um numero:"))
i = 1
while i <= 10:
    print(numero, "x", i, "=", numero *i)
    i += 1   