"""sportsday_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from sportsday import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^sportsday/activities/$', views.activities, name='activities'),
    url(r'^sportsday/matches/$', views.matches, name='matches'),
    url(r'^sportsday/create_match/$', views.create_match, name='create_match'),
    url(r'^sportsday/register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^sportsday/messages/$', views.messages, name='messages'),
    url(r'^sportsday/contact/$', views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
]
