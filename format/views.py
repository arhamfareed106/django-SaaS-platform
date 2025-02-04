from django.shortcuts import render


def home(request):
    return render(request, 'home.html')  # Renders the home.html template

def new_view(request)