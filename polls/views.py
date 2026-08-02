from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mywork(request):
    return render(request, 'mywork.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # process from (e.g., print or save)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, 'Your message has been sent!')
            return redirect('contact') # redirect to same page to clear form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})