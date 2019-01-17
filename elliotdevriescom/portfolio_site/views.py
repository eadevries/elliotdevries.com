from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import ContactMessage


def home(request):
    return render(request, 'portfolio_site/home.html')


def contact(request):
    form = ContactForm()
    return render(request, 'portfolio_site/contact.html', {'form': form})


def get_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ContactMessage(**data).save()
            return HttpResponseRedirect("{}?message-submitted=1".format(reverse('thanks')))
    else:
        form = ContactForm()
    return render(request, 'portfolio_site/contact.html', {'form': form})


def thanks(request):
    if "message-submitted" in request.GET and request.GET.get("message-submitted") == "1":
        return render(request, 'portfolio_site/thanks.html')
    else:
        return HttpResponseRedirect(reverse('home'))
