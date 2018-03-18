import os;
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sportsday_project.settings')

import django
django.setup()
from sportsday.models import Activity, Match


def populate():

    sportsday_activities = [
        {"name": "Football (5 - A Side)", "location": "G81 2XT", "numPlayers": "5", "views": "7020", "id_num": "1"},
        {"name": "Tennis (Singles)", "location": "G12 9UP", "numPlayers": "2", "views": "1310", "id_num": "2"},
        {"name": "Tennis (Doubles)", "location": "G12 9UP", "numPlayers": "4", "views": "2310", "id_num": "3"},
        {"name": "Golf (1 v 1)", "location": "G20 9HP", "numPlayers": "2", "views": "400", "id_num": "4"},
        {"name": "Badminton (Singles)", "location": "G51 4TQ", "numPlayers": "2", "views": "1520", "id_num": "5"},
        {"name": "Badminton (Doubles)", "location": "G51 4TQ", "numPlayers": "4", "views": "2661", "id_num": "6"},
        {"name": "Boxing", "location": "G52 1EQ", "numPlayers": "2", "views": "1661", "id_num": "7"},
        {"name": "Mixed Martial Arts (MMA)", "location": "G52 1EQ", "numPlayers": "2", "views": "3661", "id_num": "8"},
        {"name": "Table Tennis (Singles)", "location": "G21 3NN", "numPlayers": "2", "views": "261", "id_num": "9"},
        {"name": "Table Tennis (Doubles)", "location": "G21 3NN", "numPlayers": "2", "views": "2661", "id_num": "10"} ]

    for a in sportsday_activities:
        add_activity(a["name"], a["location"], a["numPlayers"], a["views"], a["id_num"])

def add_activity(name, location, numPlayers, views, id_num):
    a = Activity.objects.get_or_create(name=name)[0]
    a.location=location
    a.numPlayers=numPlayers
    a.views=views
    a.id_num=id_num
    a.save
    return a

if __name__ == '__main__':
    print('Starting sportsday population script...')
    populate()