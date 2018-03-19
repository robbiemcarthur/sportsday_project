import os;

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sportsday_project.settings')

import django
django.setup()
from sportsday.models import Activity, Match


def populate():

    matches = [
        {"match_id": 1, "comment": "", "activity": "1"},
        {"match_id": 2, "comment": "", "activity": "2"},
        {"match_id": 3, "comment": "", "activity": "3"},
        {"match_id": 4, "comment": "", "activity": "4"},
        {"match_id": 5, "comment": "", "activity": "5"},
        {"match_id": 6, "comment": "", "activity": "6"},
        {"match_id": 7, "comment": "", "activity": "1"},
        {"match_id": 8, "comment": "", "activity": "2"},
        {"match_id": 9, "comment": "", "activity": "3"},
        {"match_id": 10, "comment": "", "activity": "4"},
        {"match_id": 11, "comment": "", "activity": "5"},
        {"match_id": 12, "comment": "", "activity": "6"},
        {"match_id": 13, "comment": "", "activity": "1"},
        {"match_id": 14, "comment": "", "activity": "2"},
        {"match_id": 15, "comment": "", "activity": "3"},
        {"match_id": 16, "comment": "", "activity": "4"},
        {"match_id": 17, "comment": "", "activity": "5"},
        {"match_id": 18, "comment": "", "activity": "6"},
        {"match_id": 19, "comment": "", "activity": "1"},
        {"match_id": 20, "comment": "", "activity": "2"},
        {"match_id": 21, "comment": "", "activity": "3"},
        {"match_id": 22, "comment": "", "activity": "4"},
        {"match_id": 23, "comment": "", "activity": "5"},
        {"match_id": 24, "comment": "", "activity": "6"},
        {"match_id": 25, "comment": "", "activity": "1"},
        {"match_id": 26, "comment": "", "activity": "2"},
        {"match_id": 27, "comment": "", "activity": "3"},
        {"match_id": 28, "comment": "", "activity": "4"},
        {"match_id": 29, "comment": "", "activity": "5"},
        {"match_id": 30, "comment": "", "activity": "6"},
        {"match_id": 31, "comment": "", "activity": "1"},
        {"match_id": 32, "comment": "", "activity": "2"},
        {"match_id": 33, "comment": "", "activity": "3"},
        {"match_id": 34, "comment": "", "activity": "4"},
        {"match_id": 35, "comment": "", "activity": "5"},
        {"match_id": 36, "comment": "", "activity": "6"},
        {"match_id": 37, "comment": "", "activity": "1"},
        {"match_id": 38, "comment": "", "activity": "2"},
        {"match_id": 39, "comment": "", "activity": "3"},
        {"match_id": 40, "comment": "", "activity": "4"},
        {"match_id": 41, "comment": "", "activity": "5"},
        {"match_id": 42, "comment": "", "activity": "6"},
        {"match_id": 43, "comment": "", "activity": "1"},
        {"match_id": 44, "comment": "", "activity": "2"}]

    activities = [1, {"name": "Football", "location": "G81 2XT", "num_players": 5},
              2, {"name": "Tennis", "location": "G12 9UP", "num_players": 2},
              3, {"name": "Golf", "location": "G20 9HP", "num_players": 2},
              4, {"name": "Boxing", "location": "G52 1EQ", "num_players": 2},
              5, {"name": "Badminton", "location": "G51 4TQ", "num_players": 2},
              6, {"name": "Table Tennis", "location": "G21 3NN", "num_players": 2}]


    for a in activities.items():
        a = add_activity(a["number"], a["name"], a["location"], a["num_players"])
        for m in matches:
            add_match(a, m["id"], m["comment"], m["activity"])

    for a in Activity.objects.all():
        for m in Match.objects.filter(activity=l):
            print("- {0} - {1}".format(str(a), str(m)))


def add_activity(number, name, location, num_players):
    a = Activity.objects.get_or_create(number=number, name=name)[0]
    a.number=number
    a.name=name
    a.location=location
    a.num_players=num_players
    a.save
    return a

def add_match(id, comment, activity):
    m = Match.objects.get_or_create(match_id=id)[0]
    m.comment=comment
    m.activity=activity
    m.save()
    return m


if __name__ == '__main__':
    print('Starting sportsday population script...')
    populate()