from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128)
    numPlayers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    views = models.IntegerField(default=1)
    id_num = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.name


class Match(models.Model):
    activity_type = models.CharField(max_length=128)
    matches_played = models.IntegerField(default=0)
    matchnum = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.activity_type


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    password = models.CharField(default="password", max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
