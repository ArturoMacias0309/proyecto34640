from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from django.template import loader
# Create your views here.

def fam(request):
    wife = Familia(nombre = "Vanessa Diaz de Macias", birthdate ="1995-09-03", edad = 27)
    hija = Familia(nombre = "Emilia Macias Diaz", birthdate = "2019-11-11", edad = 3)
    hijo = Familia(nombre = "Javier Macias Diaz", birthdate = "2016-03-21", edad = 6)

    wife.save()
    hija.save()
    hijo.save()


    dic = {
        "nombre_wife": wife.nombre,
        "birthdate_wife": wife.birthdate,
        "edad_wife": wife.edad,
        "nombre_hija": hija.nombre,
        "birthdate_hija": hija.birthdate,
        "edad_hija": hija.edad,        
        "nombre_hijo": hijo.nombre,
        "birthdate_hijo": hijo.birthdate,
        "edad_hijo": hijo.edad
        }

    
    plantilla = loader.get_template("template1.html")
    doc = plantilla.render(dic)

    return HttpResponse(dic)