from django.shortcuts import render,HttpResponse
from libros.models import libros
from proyectotfm.models import proyectotfm

# Create your views here.
def home(request):
    return render(request,"gestionlibros/home.html")
def tusrecomendaciones(request):
    proyectotfmTest = proyectotfm.objects.all()
    return render(request,"gestionlibros/tusrecomendaciones.html",{"proyectotfms":proyectotfmTest})
def mislibros(request):
    libro=libros.objects.all()
    return render(request,"gestionlibros/mislibros.html",{"libros":libro})

