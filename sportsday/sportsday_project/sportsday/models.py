from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Activity(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    location = models.CharField(max_length=128, null=False)
    num_players = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.number
class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=128)
    activity = models.ForeignKey(Activity)

    def __str__(self):
        return self.comment

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    password = models.CharField(default="password", max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
