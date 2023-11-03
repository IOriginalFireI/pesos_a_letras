from django.shortcuts import render
from django.http import HttpResponse
from .forms import formconverter
from num2words import num2words

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "form": formconverter()
    })

def convertidof(request):
    
        
    
    dicc = {"punto": "", "cero": "", ",": "", "$": ""}
    
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
    numv11c = None
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
        
        
       
     
        
        #Cunando la cantidad termina con .01 dice "con uno centavos" (corregir)
        #Programar quitar las comas de los números que se van a ingresar
        
        #Para que no se puedan usar letras utilizar isdigit que ayuda a comprobar que determinado elemento de una cadena sea un número
        
        for palabra, valor in dicc.items():
            numv1 = numv1.replace(palabra, valor)
            numv2 = numv2.replace(palabra, valor)
            numv3 = numv3.replace(palabra, valor)
            numv4 = numv4.replace(palabra, valor)
            numv5 = numv5.replace(palabra, valor)
           
        
        if numv1:
            
             if numv1[:-3].isdigit() == False or numv1[-2:-1].isdigit() == False:
              return HttpResponse("Ingresa números en formato correcto.")
             
             if len(numv1) < 3 or numv1[-3] != ".":
              return HttpResponse("Ingresa números en formato correcto.")
             numv11 = num2words(numv1[0:-3], lang="es_CO", to="currency" )
             numv11c = num2words(numv1[-2:], lang="es_CO", to="cardinal")
             for palabra, valor in dicc.items():
                 numv11 = numv11.replace(palabra, valor)
             if numv11c == "uno":
                 numv11c = "un centavo"
             else:
                 numv11c = numv11c + " centavos"       
        if numv2:
             
             if numv2[:-3].isdigit() == False or numv2[-2:-1].isdigit() == False:
              return HttpResponse("Ingresa números en formato correcto.")
             
             if len(numv2) < 3 or numv2[-3] != ".":
              return HttpResponse("Ingresa números formato correcto.")             
             numv22 = num2words(numv2[0:-3], lang="es_CO", to="currency" )
             numv22c = num2words(numv2[-2:], lang="es_CO", to="cardinal")
             for palabra, valor in dicc.items():
                 numv2 = numv2.replace(palabra, valor)
             if numv22c == "uno":
                numv22c = "un centavo"
             else:
                numv22c = numv22c + " centavos"    
        if numv3:
             if numv3[:-3].isdigit() == False or numv3[-2:-1].isdigit() == False:
              return HttpResponse("Ingresa números en formato correcto.")
             if len(numv3) < 3 or numv3[-3] != ".":
              return HttpResponse("Ingresa números en formato correcto.")
             numv33 = num2words(numv3[0:-3], lang="es_CO", to="currency" )
             numv33c = num2words(numv3[-2:], lang="es_CO", to ="cardinal")
             for palabra, valor in dicc.items():
                 numv3 = numv3.replace(palabra, valor)
             if numv33c == "uno":
                numv33c = "un centavo"
             else:
                numv33c = numv33c + " centavos"
        if numv4:
             if numv4[:-3].isdigit() == False or numv4[-2:-1].isdigit() == False:
              return HttpResponse("Ingresa números en formato correcto.")
             if len(numv4) < 3 or numv4[-3] != ".":
              return HttpResponse("Ingresa números en formato correcto.")
             numv44 = num2words(numv4[0:-3], lang="es_CO", to="currency" )
             numv44c = num2words(numv4[-2:], lang="es_CO", to ="cardinal")
             for palabra, valor in dicc.items():
                 numv4 = numv4.replace(palabra, valor)
             if numv44c == "uno":
                 numv44c = "un centavo"
             else:
                 numv44c = numv44c + " centavos"   
        if numv5:
             if numv5[:-3].isdigit() == False or numv5[-2:-1].isdigit() == False:
              return HttpResponse("Ingresa números en formato correcto.")
             if len(numv5) < 3 or numv5[-3] != ".":
              return HttpResponse("Ingresa números en formato correcto.")
             numv55 = num2words(numv5[0:-3], lang="es_CO", to="currency" )
             numv55c = num2words(numv5[-2:], lang="es_CO", to="cardinal")
             for palabra, valor in dicc.items():
                 numv5 = numv5.replace(palabra, valor)
             if numv55c == "uno":
                 numv55c = "un centavo"
             else:
                 numv55c = numv55c + " centavos"    
    
       
        
         
       
         
                
                         
    return render (request, "resultado.html", {"numv1":numv11.capitalize(), "numv1c": numv11c, 
                                               "numv2":numv22.capitalize(), "numv2c": numv22c, 
                                               "numv3":numv33.capitalize(), "numv3c": numv33c, 
                                               "numv4":numv44.capitalize(), "numv4c": numv44c, 
                                               "numv5":numv55.capitalize(), "numv5c": numv55c, 
                                               "form":formconverter()})


                  

        
        