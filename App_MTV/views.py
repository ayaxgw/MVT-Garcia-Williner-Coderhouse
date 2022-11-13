
from App_MTV.models import Familiares
from django.http import HttpResponse

# Create your views here.

def lista_familiares(request):
    familia = Familiares.objects.all()

    vista =""
    for flia in familia:
        vista += f"({flia.nombre},{flia.cumpleaños})" + " | "
    
    return HttpResponse(vista)