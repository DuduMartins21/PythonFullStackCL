
preco = 150
desconto = 20
preco_final = preco - (preco * desconto / 100)
print("preço final após desconto:", preco_final)



peso = 70
altura = 1.75
imc = peso/(altura**2)
print(imc)


idade = 22
tem_experiencia = True
elegivel_concurso = idade >= 18 and tem_experiencia 
print("elegivel ao concurso?", elegivel_concurso)


nivel_acesso = int(input("digite seu nivel de acesso:"))
if nivel_acesso == 1:
    print("Acesso restrito")
elif nivel_acesso == 2:
    print("Acesso Parcial")
elif  nivel_acesso == 3:
    print("Acesso Total")


celsius = int(input(" digite sua temperatura"))
fahrenheit =(celsius *9/5) + 32
print(fahrenheit)



