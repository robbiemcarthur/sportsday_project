from django import forms
from django.contrib.auth.models import User
from sportsday.models import UserProfile, Match, Activity


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('activity', 'postcode', 'ability', 'available_day', 'available_time',)