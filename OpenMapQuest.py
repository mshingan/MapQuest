#Manasi Shingane 12382221 Lab Section 10 12:30- 1:50 

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'S286AgTJo75rOWkVIfrfTrJcEukfZsZg'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def build_search_url(places:list ) ->str:
    '''
    builds the mapquest url
    '''
    url_parameters = [('key', MAPQUEST_API_KEY), ('from', places[0])]
    for to_city in places[1:]:
        url_parameters.append(('to', to_city))
    return BASE_MAPQUEST_URL + urllib.parse.urlencode(url_parameters)


def build_elevation_url(latlng:str)-> str:
    '''
    builds the mapquest elevation url
    '''
    nums = ''
    url_parameters = [('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw'), ('unit', 'f'),('latLngCollection', latlng)]
    return BASE_ELEVATION_URL + urllib.parse.urlencode(url_parameters)

def get_Result(url:str) ->dict:
    '''
    gets the json response and returns it in dictionary form
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()

