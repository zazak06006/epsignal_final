from django.shortcuts import redirect, render
from .models import Info , Contact , Problem
from .forms import ContactForm , ProblemReportForm
from django.contrib.messages import constants as messages


def index(request):
    return render(request, 'acceuil.html')

def info_list(request):
    infos = Info.objects.all()  # Récupérer toutes les infos
    return render(request, 'info_list.html', {'infos': infos})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            #Envoie mail contact


            return redirect('index') 
        form = ContactForm()

    return render(request, 'contact.html')


def signaler_view(request):
    if request.method == 'POST':
        form = ProblemReportForm(request.POST)
        if form.is_valid():
            #Envoie mail signaler

            
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to a 'home' page or any other page after successful submissio
        form = ProblemReportForm()
    
    return render(request, 'signaler.html')