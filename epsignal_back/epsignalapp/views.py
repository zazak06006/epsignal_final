from django.shortcuts import redirect, render 
from .models import Info , Contact , Problem , Newsletter
from .forms import ContactForm , ProblemReportForm , NewsletterForm
from django.contrib import messages
from datetime import datetime
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Votre action a été réalisée avec succès.')
        form = ContactForm()
    return render(request, 'acceuil.html')

def info_list(request):
    infos = Info.objects.all()  # Récupérer toutes les infos
    return render(request, 'info_list.html', {'infos': infos})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email_contact(
            request.POST.get('name'),
            request.POST.get('surname'),
            request.POST.get('email'),
            request.POST.get('subject'),
            request.POST.get('message'),
            )
            form.save() 
            messages.success(request, 'Votre action a été réalisée avec succès.')
        return redirect('index')
        form = ContactForm()

    return render(request, 'Contact.html')


def signaler_view(request):

    if request.method == 'POST':

        print(request.POST)
        form = ProblemReportForm(request.POST)
        if form.is_valid():
            print("okkkkkkkkkkkkk")
            send_email(
                request.POST.get('problem_type'), 
                request.POST.get('email'),
                request.POST.get('description'),
                )
            messages.success(request, "Votre action a été réalisée avec succès.")
            form.save() # Save the form data to the database
            return redirect('index')
        else:
            print("erreruerrr")  # Redirect to a 'home' page or any other page after successful submissio
        form = ProblemReportForm()
    
    return render(request, 'signaler.html')


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(problem_type,email, message):
    # Déterminez l'email du destinataire en fonction du type de problème
    if problem_type == "technique":
        recipient_email = "technicien.epsi2024@gmail.com"
    elif problem_type == "physique":
        recipient_email = "espib32024@gmail.com"
    else:
        print("Type de problème invalide.")
        return

    # Créez le message
    subject = f"Signalement de problème : {problem_type.capitalize()}"
    body = f"""
    Type de problème : {problem_type}
    Email : {email}
    Description : {message}
    """

    # Configuration de l'email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Envoyer l'email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('epsib32024@gmail.com', 'qflr cxqv enls xljn ')  # Remplacez par votre email et mot de passe
            server.send_message(msg)
            print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")


def send_email_contact(name, phone, email, subject, message):
    # Déterminez l'email du destinataire en fonction du type de problème
    recipient_email = "marouanekaidi@gmail.com"
    # Créez le message
    subject = f"Contact : {subject.capitalize()}"
    body = f"""
    Nom : {name}
    Phone : {phone}
    Email : {email}
    message : {message}
    """

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Envoyer l'email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('epsib32024@gmail.com', 'qflr cxqv enls xljn ')  # Remplacez par votre email et mot de passe
            server.send_message(msg)
            print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")