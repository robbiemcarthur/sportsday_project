from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context_dict = {'boldmessage': "Welcome to SportsDay!"}
    return render(request, 'sportsday/home_page.html', context=context_dict)

def activities(request):
    return render(request, 'sportsday/activities.html')

def matches(request):
    return render(request, 'sportsday/matches.html')

def register(request):
    return render(request, 'sportsday/register.html')

def messages(request):
    return render(request, 'sportsday/messages.html')

def contact(request):
    return render(request, 'sportsday/contact.html')
