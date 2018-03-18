from django.contrib import admin
from sportsday.models import Category, Page, UserProfile, Activity, Match, Message

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Match)
admin.site.register(Message)