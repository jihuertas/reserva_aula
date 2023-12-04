from django.shortcuts import render, redirect
from .models import Aula
from .forms import ReservaAulaForm# Create your views here.
# Create your views here.

def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'appreserva/lista_aulas.html', {'aulas': aulas})

def reserva_aula(request):
    if request.method == 'POST':
        form = ReservaAulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aulas')  
    else:
        form = ReservaAulaForm()
    return render(request, 'appreserva/reserva_aulas.html', {'form': form})