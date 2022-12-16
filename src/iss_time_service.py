import requests
import time
from geopy.geocoders import Nominatim
from string import Template


def get_response():
    return requests.get("http://api.open-notify.org/iss-now.json").json()

def parse_response(json):
    return [json["timestamp"], [float(json["iss_position"]["longitude"]), float(json["iss_position"]["latitude"])]]

def convert_timestamp_to_ct_time(timestamp):
    ct = time.ctime(timestamp)[11:16]
    hrs = ct[0:2]
    if int(hrs) > 12:
        am_pm = 'PM'
        hrs = str(int(hrs) - 12)
    else:
        am_pm = 'AM'
        
    minutes = ct[3:5]
    result = Template('$hrs:$minutes$am_pm')
    return (result.substitute({'hrs': hrs, 'minutes': minutes, 'am_pm': am_pm}))
 
def convert_coordinates_to_city_state(coordinates):
    input_coordinates = str(coordinates[1]) + ',' + str(coordinates[0])
    geolocator = Nominatim(user_agent="walters_hiller")
    location = geolocator.reverse(input_coordinates)
    
    if bool(location) is False:
        return 'None'
    else:
        address = location.raw['address']
        city= address.get('city', '')
        state = address.get('state', '')
        return city + ', ' + state
        
def get_location():
    time_location =  parse_response(get_response())
    return [convert_timestamp_to_ct_time(time_location[0]), convert_coordinates_to_city_state(time_location[1])]
