from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Later you can add email sending or save to DB here

        messages.success(request, "Message sent successfully!")
        return redirect('home')

    return redirect('home')