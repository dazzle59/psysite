from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('articles.html', views.articles, name='articles'),
    path('contacts.html', views.contacts, name='contacts'),
    path('diploms.html', views.diploms, name='diploms'),
    path('price.html', views.price, name='price'),
    path('services.html', views.services, name='services'),
    path('contact.html', views.contact, name='contact'),
    path('ok.html', views.ok, name='ok')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)