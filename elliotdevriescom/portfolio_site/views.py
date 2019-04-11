from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import ContactForm
from .models import ContactMessage, Project


def home(request):
    featured_projects = Project.objects.order_by('order')[:3]
    return render(request, 'portfolio_site/home.html', {'featured_projects': featured_projects})


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


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio_site/project.html', {'project': project})


def thanks(request):
    if "message-submitted" in request.GET and request.GET.get("message-submitted") == "1":
        return render(request, 'portfolio_site/thanks.html')
    else:
        return HttpResponseRedirect(reverse('home'))
