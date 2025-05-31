from django.contrib import admin
from .models import Produto
from .models import Plano
from .models import Contato

admin.site.register(Produto)
admin.site.register(Plano)
admin.site.register(Contato)
# Register your models here.

