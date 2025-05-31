from django import forms
from .models import Produto, UserProfile, Contato

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'imagem', 'preco']  # Campos do formulário

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']  # Apenas o campo de foto

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
