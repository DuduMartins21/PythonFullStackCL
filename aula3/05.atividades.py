#Cada numeração corresponde a um programa diferente para que seja desenvolvido. As atividades seguem abaixo:

#1.Filtre produtos com preço > 1000 usando list comprehension;

 
produtos = [
    {"nome": "Computador", "preco": 1200, "categoria": "Informática"},
    {"nome": "Laptop", "preco": 800, "categoria": "Informática"},
    {"nome": "Celular", "preco": 1500, "categoria": "Informática"},
    {"nome": "Sofá", "preco": 1001, "categoria": "Móveis"}
]
produtos_caros = [produto for produto in produtos if produto["preco"] > 1000]
print(produtos_caros)


#2.Conte quantos produtos existem por categoria (usar dicionário);


contagem = {}

for produto in produtos:
    categoria = produto["categoria"]
    if categoria in contagem:
        contagem[categoria] += 1
    else:
        contagem[categoria] = 1

        print(contagem)

 
    
#3.Remova duplicatas de uma lista de pedidos usando set.
        

produtos = [
    {"nome": "Computador", "preco": 1200, "categoria": "Informática"},
    {"nome": "Laptop", "preco": 800, "categoria": "Informática"},
    {"nome": "Celular", "preco": 1500, "categoria": "Informática"},
    {"nome": "Sofá", "preco": 1001, "categoria": "Móveis"}
]

pedidos = ["Computador", "Laptop", "Celular", "Sofá", "Laptop", "Celular"]
Remover_duplicatas = list(set(pedidos))
print(Remover_duplicatas)

#4.Uma empresa contratou seus serviços para armazenar dados de colaboradores em memória e realizar operações como:
'''
Adicionar novos colaboradores.
Buscar colaborador por ID.
Listar colaboradores com salário acima de X.
'''
#Implemente utilizando funções.