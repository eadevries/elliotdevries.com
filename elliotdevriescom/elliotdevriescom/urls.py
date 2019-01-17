from django.contrib import admin
from django.urls import path

from portfolio_site.views import contact, get_message, home, thanks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('get_message/', get_message, name='get_message'),
    path('thanks', thanks, name='thanks')
]
