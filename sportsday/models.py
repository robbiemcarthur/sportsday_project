from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    numPlayers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    availability = models.DateTimeField(auto_now=False, auto_now_add=False)
    views = models.IntegerField(default=0)
    id_num = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    players = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    activity_type = models.CharField(max_length=128)
    availability = models.DateTimeField(auto_now=False, auto_now_add=False)
    views = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    id_num = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Message(models.Model):
    message = models.CharField(max_length=256)

    def __str__(self):
        return self.message


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
