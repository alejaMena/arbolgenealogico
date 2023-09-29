from django.shortcuts import render, redirect
from .forms import PersonaForm, ParentescoForm, MatrimonioForm

def persona_form(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:persona_form')  # Puedes redirigir a donde necesites
    else:
        form = PersonaForm()
    return render(request, 'genealogia/persona_form.html', {'form': form})

def parentesco_form(request):
    if request.method == 'POST':
        form = ParentescoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:parentesco_form')  # Puedes redirigir a donde necesites
    else:
        form = ParentescoForm()
    return render(request, 'genealogia/parentesco_form.html', {'form': form})

def matrimonio_form(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genealogia:matrimonio_form')  # Puedes redirigir a donde necesites
    else:
        form = MatrimonioForm()
    return render(request, 'genealogia/matrimonio_form.html', {'form': form})