# Questão 1

numero = int(input("Digite um número para a contagem regressiva: "))
for i in range(numero, -1, -1):
    print(i)


# Questão 2

numero = int(input("Digite um número para somar de 1 até ele: "))
soma = 0
i = 1
while i <= numero:
    soma += i
    i += 1
print("Soma:", soma)


# Questão 3

numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Questão 4

numero = int(input("Digite um número para ver os pares até ele: "))
for i in range(2, numero + 1, 2):
    print(i)


# Questão 5

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
print(f"Fatorial de {numero}: {fatorial}")


# Questão 6

numero = 0
while numero <= 10:
    numero = int(input("Digite um número maior que 10: "))
print("Número válido:", numero)


# Questão 7

tamanho = int(input("Digite o tamanho do quadrado: "))
for i in range(tamanho):
    for j in range(tamanho):
        print("*", end=" ")
    print()