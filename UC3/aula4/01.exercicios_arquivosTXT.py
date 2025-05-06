
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Nome: Carlos\ne-mail: cdudusm@gmail.com\n")
    arquivo.write("Nome: João\ne-mail: joão@gmail.com\n")

with open('arquivo.txt' ,'r') as dados:
    conteudo = dados.read()
    print(conteudo)

import os
if os.path.exists('arquivo.txt'):
    os.remove('arquivo.txt')
    print("Arquivo removido!")
else:
    print("Arquivo não encontrado.")