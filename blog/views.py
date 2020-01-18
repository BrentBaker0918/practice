#practice/views.def

from django.http import HttpResponse

def index(request):
    return HttpResponse('Django Blog')
