import json
import requests


def retrieve_coordinates(zipcode):
    req = requests.request('GET', 'http://api.openweathermap.org/geo/1.0/zip?zip=' + zipcode + ',US&appid=ce3cc47717e5e'
                                                                                               '239c048e33936caa91e')
    return json.loads(req.content)


def retrieve_weather(lat, long):
    req = requests.request('GET', 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + long +
                           '&units=imperial&exclude=minutely,alerts&appid=ce3cc47717e5e239c048e33936caa91e')
    parsed_req = json.loads(req.content)
    print(parsed_req['current'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    location = retrieve_coordinates('14623')
    retrieve_weather(str(location['lat']), str(location['lon']))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
