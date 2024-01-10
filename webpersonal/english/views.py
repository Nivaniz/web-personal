from django.shortcuts import render
from .models import ProjectEnglish
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def main(request):
    return render(request, "english/main.html")

def aboutme(request):
    return render(request, "english/aboutme.html")

# views.py
def portfoliome(request):
    projects = ProjectEnglish.objects.all()
    print("Projects:", projects)  # Añade este print para verificar los proyectos en la consola
    recent_projects = ProjectEnglish.objects.order_by('-created')[:3]
    return render(request, "english/portfoliome.html", {'projects': projects, 'recent_projects': recent_projects})

def contactme(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                "Codingwithnirvana: Nuevo mensaje de contacto",
                "De: {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["nivaniz2019@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                return redirect(reverse('contact') + '?fail')

    return render(request, "english/contactme.html", {'form': contact_form})