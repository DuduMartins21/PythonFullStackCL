from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Site do SenacRj - APP 02</h1>")

def franquia(request):
    return HttpResponse("<h1>Site da Franquia - APP 02</h1>")

def faleconosco(request):
    return HttpResponse("<h1>Site da Fale conosco - APP 02</h1>")