

import json
from urllib.request import urlopen
import os
import datetime

response = urlopen('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')
data = json.dumps(str('mag'))
data = json.load(response)
earthquakes = data['features']


def quake(earthquakes):
    for earthquake in earthquakes:
        magnitude = earthquake['properties']['mag']
        epoch_time = earthquake['properties']['time']
        place = earthquake['properties']['place']
        t = epoch_time / 1000.0
        time = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M%:%S.%f')
        now = datetime.datetime.today()
        run = True
        while run:
            if time == now and place.endswith("CA") and magnitude < 7.0:
                title = "Earthquake Alert"
                text = magnitude, place
                return text
            elif time == now and place.endswith("CA") and magnitude > 7.0:
                text = (magnitude, "SEEK SHELTER NOW")
                return text
            else:
                pass


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(title, text))


# quake(earthquakes)
title, text = quake(earthquakes)
notify("Earthquake Alert", "{}   |   {}".format(title, text))
