from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from sportsday.models import Activity, Match
from sportsday.forms import UserForm, UserProfileForm, MatchForm


def home_page(request):
    context_dict = {'boldmessage': "Welcome to SportsDay!"}
    return render(request, 'sportsday/home_page.html', context=context_dict)


def activities(request):
    activity_list = Activity.objects.all()
    context_dict = {'activities': activity_list}
    return render(request, 'sportsday/activities.html', context_dict)


def matches(request):
    match_list = Match.objects.all()
    context_dict = {'matches': match_list}
    return render(request, 'sportsday/matches.html', context_dict)


def create_match(request):
    if request.method == 'POST':
        match_form = MatchForm(data=request.POST)
        match = match_form.save()
        match.save()
    else:
        match_form = MatchForm()

    return render(request, 'sportsday/create_match.html', {'match_form': match_form})


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home_page'))
            else:
                return HttpResponse('Disabled')
        else:
            print("incorrect login details")
            return HttpResponse("Incorrect Login.")
    else:
        return render(request, 'sportsday/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Only logged in users can see this.")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))


def messages(request):
    return render(request, 'sportsday/messages.html')


def contact(request):
    return render(request, 'sportsday/contact.html')
