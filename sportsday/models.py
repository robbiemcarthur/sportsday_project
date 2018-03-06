from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    id = models.IntegerField(default=0, unique=True)

    def __str__(self):
    return self.name

class Matches(models.Model):
    name = models.CharField(max_length=128, unique=True)
    players = models.IntegerField(default=0, max=2)
    views = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    id = models.IntegerField(default=0, unique=True)

class Page(models.Model):
    activity = models.ForeignKey(Activity)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
            return self.user.username
