from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def reference(request):
    return render(request, 'reference.html')

def gallery(request):
    return render(request, 'gallery.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(
                request,
                "Thank you! Your message has been sent successfully."
            )
            form = ContactForm()

    return render(request, 'contact.html', {"form": form})
