from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from datetime import datetime

def fecha_actual(request):
    hoy = datetime.now().strftime("%Y/%m/%d")
    return HttpResponse(hoy)

def inicio(request):
    # Leemos el contenido del archivo HTML
    archivo = open(r'MTV_GW\templates\inicio.html')
    
    # Creamos una plantilla a partir del contenido del archivo
    plantilla = Template(archivo.read())
    
    # Cerramos el archivo porque no lo usamos mas
    archivo.close()
    
    # Diccionario con datos para la plantilla
    datos = {"nombre": "Ayax", "fecha": datetime.now(), "apellido":"Garcia Williner"}

    # Creamos el contexto que necesita la plantilla
    contexto = Context(datos)

    # Generar el documento a devolver al usuario
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_familiares(request):
    # Abrimos el archivo
    archivo = open(r'MTV_GW\templates\listado_familiares.html')
    
    # Creamos el template
    plantilla = Template(archivo.read())

    # Cerramos el archivo

    archivo.close()

    # Creamos el diccionario de datos
    listado_familiares = ["F. Garcia Williner","M. Williner", "J. Garcia","Z. Williner","O.I. Williner"]
    
    datos = {"Informacion":"Datos", "listado_familiares":listado_familiares}

    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
    
def vista_listado_familiares2(request):
    listado_familiares = ["F. Garcia Williner","M. Williner", "J. Garcia","Z. Williner","O.I. Williner"]
    datos = {"Informacion":"Datos", "listado_familiares":listado_familiares}
    
    plantilla = loader.get_template(r"listado_familiares.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

    