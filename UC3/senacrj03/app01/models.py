from django.db import models

# app01/models.py


class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='cursos_imagens/', null=True, blank=True) # Opcional: para adicionar uma imagem
    data_publicacao = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False) # Para a sua home, se você ainda usar

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-data_publicacao'] # Ordena os cursos pelo mais recente primeiro

    def __str__(self):
        return self.titulo




class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True) # Vai registrar a data e hora do envio automaticamente

    class Meta:
        verbose_name = "Contato" # Nome que aparece no admin (singular)
        verbose_name_plural = "Contatos" # Nome que aparece no admin (plural)
        ordering = ['-data_envio'] # Ordena os contatos do mais recente para o mais antigo

    def __str__(self):
        # Como o objeto será representado no admin (ex: "Mensagem de Carlos (carlos@email.com)")
        return f"Mensagem de {self.nome} ({self.email})"

# Certifique-se de que a sua classe Curso ainda esteja aqui (se você já a tinha):
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens_cursos/', blank=True, null=True)

    def __str__(self):
        return self.titulo