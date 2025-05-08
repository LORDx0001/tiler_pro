# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, Testimonial
from .forms import ContactForm
import requests
def home(request):
    services = Service.objects.all()[:3]  # Get first 3 services
    projects = Project.objects.all().order_by('-date_completed')[:8]  # Get latest 8 projects
    testimonials = Testimonial.objects.all()[:3]  # Get 3 testimonials
    
    # Handle contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will contact you soon!')
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'tiler_app/home.html', context)

def services(request):
    services = Service.objects.all()
    return render(request, 'tiler_app/services.html', {'services': services})

def gallery(request):
    projects = Project.objects.all().order_by('-date_completed')
    return render(request, 'tiler_app/gallery.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender(form.cleaned_data)
            messages.success(request, 'Your message has been sent. We will contact you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'tiler_app/contact.html', {'form': form})

bot_token = '7939886196:AAHOJhfrXpaKNjHoRl7MuKUPGVDR1LZ28Ak'
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

def sender(data):
    text = ""
    for key, value in data.items():
        text += f'{key}: {value}\n'
    params = {
        "chat_id": -4630075533,
        "text": text,
    }
    response = requests.post(url, params=params)
    return response.status_code == 200
