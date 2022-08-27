from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido.")

def suma(request, primer_operando, segundo_operando):
    operacion = primer_operando + segundo_operando
    return HttpResponse("La suma de %s + %s = %s" % (primer_operando, segundo_operando, operacion))

def resta(request, primer_operando, segundo_operando):
    operacion = primer_operando - segundo_operando
    return HttpResponse("La resta de %s - %s = %s" % (primer_operando, segundo_operando, operacion))

def multiplicacion(request, primer_operando, segundo_operando):
    operacion = primer_operando * segundo_operando
    return HttpResponse("La multiplicacion de %s * %s = %s" % (primer_operando, segundo_operando, operacion))