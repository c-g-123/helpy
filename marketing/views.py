from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# Is this view really necessary?
# def contact(request):
#     return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')
