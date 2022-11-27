from django.shortcuts import render,redirect
from rEquipos.forms import FormEquipo
from rEquipos.models import Equipos
# Create your views here.


def index(request):
    return render(request,'rEquipos/index.html')

def listadoEquipos(request):
    equipos = Equipos.objects.all()
    data = {"equipos":equipos}
    return render(request,'rEquipos/equipos.html',data)

def agregarEquipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'rEquipos/registrarEquipo.html',data)

#Funciones

def eliminarEquipo(request,id):
    equipos=Equipos.objects.get(id=id)
    equipos.delete()
    return redirect('/equipos')


def actualizarEquipo(request,id):
    equipo = Equipos.objects.get(id=id)
    form = FormEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'rEquipos/registrarEquipo.html',data)




#pantalla carga