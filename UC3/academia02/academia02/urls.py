"""
URL configuration for academia02 project.

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
from django.contrib import admin
from django.urls import path, include
from app01.views import home, produtos, contatos  # Importe a view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls')),  # Inclui as URLs do meuapp
    path('', home, name='home'),  # Rota principal
    path('produtos/', produtos, name='produtos'),  # Rota para produtos
    path('contatos/', contatos, name='contatos'),  # Rota para contato
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




