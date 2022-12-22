from django.http import HttpResponse
def NombreApp(response): #Vista1 saludo
    return HttpResponse("Bienvenidos Rereadlovers!")

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



