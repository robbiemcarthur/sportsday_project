<<<<<<< HEAD
from django.contrib import admin
from sportsday.models import UserProfile, Activity, Match

admin.site.register(UserProfile)
admin.site.register(Activity)
=======
from django.contrib import admin
from sportsday.models import Activity, Match

admin.site.register(Activity)
>>>>>>> 75b4756a7df7653ad2a4740830138b6f1e547be3
admin.site.register(Match)