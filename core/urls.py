from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('socios/', views.socios, name='socios'),
    path('servicios/', views.servicios, name='servicios'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
    path('afiliacion/', views.afiliacion, name='afiliacion'),
    path('login/', views.login, name='login'),
]