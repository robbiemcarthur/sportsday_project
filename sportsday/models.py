from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Match(models.Model):
    activity = models.ForeignKey(Activity)
    postcode = models.CharField(max_length=128)
    url = models.URLField()
    ability = models.CharField(max_length=128)
    available_day = models.CharField(max_length=128)
    available_time = models.CharField(max_length=128)
    players = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.postcode


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username