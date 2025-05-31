"""
URL configuration for senacrj03 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# seu_projeto/urls.py

from django.contrib import admin
from django.urls import path
from app01.views import home, cursos, contatos

# Adicione estas duas linhas de importação:
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cursos/', cursos, name='cursos'),
    path('contatos/', contatos, name='contatos')
]

# Seu bloco condicional para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT if settings.STATIC_ROOT else settings.STATICFILES_DIRS[0]) # Adicione esta linha também, ou ajuste conforme sua configuração

