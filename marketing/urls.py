from django.urls import path

from marketing import views


app_name = 'marketing'


urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Is this page really necessary?
    # path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]
