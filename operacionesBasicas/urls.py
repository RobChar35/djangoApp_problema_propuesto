from unittest import result
from django.urls import path
from . import views

urlpatterns = [
    #Principal
    path('', views.index, name='index'),

    #Suma
    path('suma/<int:primer_operando>/<int:segundo_operando>/', views.suma, name='suma'),

    #Resta
    path('resta/<int:primer_operando>/<int:segundo_operando>/', views.resta, name='resta'),

    #Multiplicacion
    path('multiplicacion/<int:primer_operando>/<int:segundo_operando>/', views.multiplicacion, name='multiplicacion'),

]