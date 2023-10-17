from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import formconverter
from num2words import num2words

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "form": formconverter()
    })



def convertidof(request):
    
    dicc = {"punto": "", "cero": "" }
    diccc = {"pesos": "" }
    
    numv1 = None
    numv2 = None
    numv3 = None
    numv4 = None
    numv5 = None
    numv11 = ""
    numv22 = ""
    numv33 = ""
    numv44 = ""
    numv55 = ""
    numv11c = "cero"
    numv22c = None
    numv33c = None
    numv44c = None
    numv55c = None
    
    if request.method == "POST":
        
        numv1 = request.POST.get("num1")
        numv2 = request.POST.get("num2")
        numv3 = request.POST.get("num3")
        numv4 = request.POST.get("num4")
        numv5 = request.POST.get("num5")
        
          
        
        if numv1 [-2:-1] == "00":
             numv11 = num2words(numv1[0:-3], lang="es_CO", to="currency" )   #Con .00 que diga con cero centavos
             numv11c = num2words(numv1[-2:], lang="es_CO", to="currency")    # Quitar las comas de los números introducidos
             for palabra, valor in dicc.items():
                 numv1 = numv1.replace(palabra, valor)
             for palabra, valor in diccc.items():
                 numv11c= numv11c.replace(palabra,valor)    
                 
        else:
            numv11 = num2words(numv1, lang="es_CO", to="currency" )              
        
        if numv2:
             numv22 = num2words(numv2[0:-3], lang="es_CO", to="currency" )
             numv22c = num2words(numv2[-2:], lang="es_CO", to="cardinal")
             for palabra, valor in dicc.items():
                 numv2 = numv2.replace(palabra, valor)
        if numv3:
             numv33 = num2words(numv3[0:-3], lang="es_CO", to="currency" )
             numv33c = num2words(numv3[-2:], lang="es_CO")
             for palabra, valor in dicc.items():
                 numv3 = numv3.replace(palabra, valor)
        if numv4:
             numv44 = num2words(numv4[0:-3], lang="es_CO", to="currency" )
             numv44c = num2words(numv4[-2:], lang="es_CO")
             for palabra, valor in dicc.items():
                 numv4 = numv4.replace(palabra, valor)
        if numv5:
             numv55 = num2words(numv5[0:-3], lang="es_CO", to="currency" )
             numv55c = num2words(numv5[-2:], lang="es_CO")
             for palabra, valor in dicc.items():
                 numv5 = numv5.replace(palabra, valor)        
            
            
                
    return render (request, "resultado.html", {"numv1":numv11.capitalize(), "numv1c": numv11c, 
                                               "numv2":numv22.capitalize(), "numv2c": numv22c, 
                                               "numv3":numv33.capitalize(), "numv3c": numv33c, 
                                               "numv4":numv44.capitalize(), "numv4c": numv44c, 
                                               "numv5":numv55.capitalize(), "numv5c": numv55c, 
                                               "form":formconverter()})


                  

        
        