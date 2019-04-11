from django.contrib import admin
from django.urls import path

# from portfolio_site.views import contact, get_message, home, project, thanks
from portfolio_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('get_message/', views.get_message, name='get_message'),
    path('project/<slug:slug>/', views.project, name='project'),
    path('thanks', views.thanks, name='thanks')
]
