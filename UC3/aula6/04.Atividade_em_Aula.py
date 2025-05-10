# Atividades Práticas:

# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''


# classe chamada Conta, que vai representar uma conta com saldo.
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):            # Esta parte permite acessar o saldo usando 'conta.saldo' como se fosse um atributo comum.
        return self._saldo      # Ele retorna o valor armazenado em _saldo (sem formatação, ainda como número).
    
    @saldo.setter
    def saldo(self, valor):      # Aqui estamos dizendo: se o novo valor do saldo for maior ou igual a zero,
        if valor >= 0:           # podemos atualizar o saldo. Se for negativo, mostramos um erro.
            self._saldo = valor
        else:
            raise ValueError("O saldo não pode ser negativo")


valor = float(input("Digite o saldo: "))
conta = Conta(valor)    # Criamos uma nova conta usando o valor que o usuário digitou.
print(f"Saldo da conta: R${conta.saldo:.2f}")   # Agora mostramos o saldo formatado com duas casas decimais.




# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''
class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def brincar(self):
        return  f"{self.nome} está brincando"

    def comer(self):
        if self.raca == "cacchorro":
            return f"{self.raca} esta comendo ração para cães"
        elif self.raca == "gato":
            return f"{self.raca} esta comendo ração para gatos"
        else:
            return f"esta comendo ração"
         


# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''





# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.