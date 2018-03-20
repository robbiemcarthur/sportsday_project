import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sportsday_project.settings')

import django
django.setup()
from sportsday.models import Activity, Match


def populate():
    hiking_matches = [
        {"location": "G81 2XT",
         "url": "https://www.goalsfootball.co.uk/clubs/scotland/glasgow-west/",
         "views": 123}]

    tennis_matches = [
        {"location": "G12 9UP",
         "url": "http://www.glasgowwestern.co.uk/",
         "views": 123}]

    golf_matches = [
        {"location": "G20 9HP",
         "url": "https://www.glasgowlife.org.uk/sport/golf/play/pages/ruchill.aspx",
         "views": 123}]

    boxing_matches = [
        {"location": "G52 1EQ",
         "url": "http://www.bellahoustonboxingclub.co.uk/bella_wp/",
         "views": 123}]

    badminton_matches = [
        {"location": "G51 4QT",
         "url": "http://www.badmintonscotland.org.uk/contact/",
         "views": 123}]

    table_tennis_matches = [
        {"location": "G81 2XT",
         "url": "https://www.glasgowlife.org.uk/sport/table-tennis/pages/default.aspx",
         "views": 123}]

    acts = {"Hiking": {"activities": hiking_matches, "views" : 128, "likes" : 64},
            "Tennis": {"activities": tennis_matches, "views" : 128, "likes" : 64},
            "Golf": {"activities": golf_matches, "views" : 128, "likes" : 64},
            "Boxing": {"activities": boxing_matches, "views" : 128, "likes" : 64},
            "Badminton": {"activities": badminton_matches, "views" : 128, "likes" : 64},
            "Table Tennis": {"activities": table_tennis_matches, "views" : 128, "likes" : 64}}

    for act, act_data in acts.items():
        a = add_activity(act, act_data["views"], act_data["likes"])
        for m in act_data["activities"]:
            add_match(a, m["location"], m["url"], m["views"])

    for a in Activity.objects.all():
        for m in Match.objects.filter(activity=a):
            print("- {0} - {1}".format(str(a), str(m)))



def add_match(act, location, url, views):
    m = Match.objects.get_or_create(activity=act, location=location)[0]
    m.url = url
    m.views = views
    m.save()
    return m

def add_activity(name, views, likes):
    a = Activity.objects.get_or_create(name=name)[0]
    a.likes = likes
    a.views = views
    a.save()
    return a

if __name__ == '__main__':
    print('Starting sportsday population script...')
    populate()