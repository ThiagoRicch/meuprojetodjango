from django.http import HttpResponse

def home_views(request):
    return HttpResponse('<h1>Meu Projeto</h1>')

