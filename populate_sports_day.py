import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sportsday_project.settings')

import django
django.setup()
from sportsday.models import Activity, Match


def populate():
    hiking_matches = [
        {"postcode": "G51 1RN",
         "url": "https://www.glasgowclimbingcentre.com/",
         "ability": "Expert",
         "available_day": "Monday",
         "available_time": "09:00 - 12:00",
         "players": 2,
         "match_number": 1,
         "views": 27},
        {"postcode": "G41 1EJ",
         "url": "https://www.theclimbingacademy.com/our-walls/glasgow/",
         "ability": "Beginner",
         "available_day": "Wednesday",
         "available_time": "13:00 - 17:00",
         "players": 2,
         "match_number": 2,
         "views": 44}
    ]

    tennis_matches = [
        {"postcode": "G12 9UP",
         "url": "http://www.glasgowwestern.co.uk/",
         "ability": "Beginner",
         "available_day": "Tuesday",
         "available_time": "10:00 - 11:00",
         "players": 2,
         "match_number": 1,
         "views": 73},
        {"postcode": "G12 9UP",
         "url": "http://www.glasgowwestern.co.uk/",
         "ability": "Intermediate",
         "available_day": "Tuesday",
         "available_time": "10:00 - 12:00",
         "players": 2,
         "match_number": 2,
         "views": 91},
        {"postcode": "G42 9QL",
         "url": "https://www.queensparkctc.org/live/pages/welcome.php",
         "ability": "Expert",
         "available_day": "Thursday",
         "available_time": "14:00 - 15:00",
         "players": 2,
         "match_number": 3,
         "views": 87},
        {"postcode": "G42 9QL",
         "url": "https://www.queensparkctc.org/live/pages/welcome.php",
         "ability": "Beginner",
         "available_day": "Thursday",
         "available_time": "18:00 - 19:00",
         "players": 2,
         "match_number": 4,
         "views": 65}
    ]

    golf_matches = [
        {"postcode": "G20 9HP",
         "url": "https://www.glasgowlife.org.uk/sport/golf/play/pages/ruchill.aspx",
         "ability": "Expert",
         "available_day": "Friday",
         "available_time": "09:00 - 14:00",
         "players": 2,
         "match_number": 1,
         "views": 188},
        {"postcode": "G20 9HP",
         "url": "https://www.glasgowlife.org.uk/sport/golf/play/pages/ruchill.aspx",
         "ability": "Beginner",
         "available_day": "Thursday",
         "available_time": "18:00 - 19:00",
         "players": 2,
         "match_number": 4,
         "views": 65}
    ]

    boxing_matches = [
        {"postcode": "G52 1EQ",
         "url": "http://www.bellahoustonboxingclub.co.uk/bella_wp/",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 123}]

    badminton_matches = [
        {"postcode": "G51 4QT",
         "url": "http://www.badmintonscotland.org.uk/contact/",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 123}]

    table_tennis_matches = [
        {"postcode": "G81 2XT",
         "url": "https://www.glasgowlife.org.uk/sport/table-tennis/pages/default.aspx",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 123}]

    squash_matches = [
        {"postcode": "",
         "url": "",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 12}
    ]

    rockclimbing_matches = [
        {"postcode": "",
         "url": "",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 12}
    ]

    running_matches = [
        {"postcode": "",
         "url": "",
         "ability": "",
         "available_day": "",
         "available_time": "",
         "players": 2,
         "match_number": 1,
         "views": 12}
    ]

    acts = {"Hiking": {"activities": hiking_matches, "views" : 128, "likes" : 64},
            "Tennis": {"activities": tennis_matches, "views" : 128, "likes" : 64},
            "Golf": {"activities": golf_matches, "views" : 128, "likes" : 64},
            "Boxing": {"activities": boxing_matches, "views" : 128, "likes" : 64},
            "Badminton": {"activities": badminton_matches, "views" : 128, "likes" : 64},
            "Table Tennis": {"activities": table_tennis_matches, "views" : 128, "likes" : 64},
            "Squash": {"activities": squash_matches, "views" : 192, "likes": 20},
            "Rock Climbing": {"activities" : rockclimbing_matches, "views": 212, "likes": 150},
            "Running": {"activities": running_matches, "views": 1242, "likes": 1729}}

    for act, act_data in acts.items():
        a = add_activity(act, act_data["views"], act_data["likes"])
        for m in act_data["activities"]:
            add_match(a, m["location"], m["url"], m["ability"], m["available_day"], m["available_time"], m["players"], m["views"])

    for a in Activity.objects.all():
        for m in Match.objects.filter(activity=a):
            print("- {0} - {1}".format(str(a), str(m)))


def add_match(act, postcode, url, ability, available_day, available_time, players, views):
    m = Match.objects.get_or_create(activity=act, postcode=postcode)[0]
    m.url = url
    m.ability = ability
    m.available_day = available_day
    m.available_time = available_time
    m.players = players
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