from django.shortcuts import render
from django.http import HttpResponse
from sportsday.models import Activity, Match
from sportsday.forms import UserForm, UserProfileForm

def home_page(request):
    context_dict = {'boldmessage': "Welcome to SportsDay!"}
    return render(request, 'sportsday/home_page.html', context=context_dict)

def activities(request):
    activity_list = Activity.objects.order_by('-likes')
    context_dict = {'activities': activity_list}
    return render(request, 'sportsday/activities.html', context_dict)

def matches(request):
    return render(request, 'sportsday/matches.html')

def create_match(request):
    return render(request, 'sportsday/create_match.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'sportsday/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def messages(request):
    return render(request, 'sportsday/messages.html')

def contact(request):
    return render(request, 'sportsday/contact.html')
