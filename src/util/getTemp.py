


import requests
from os import getenv

def makeURL(location:str):
    return f'https://api.weatherapi.com/v1/current.json?key={getenv("API_KEY")}&q={location}&aqi=no'


def getTemperature(location:str):
    api_url:str = makeURL(location=location)
    response = requests.get(api_url)
    response.raise_for_status()
    weather_data = response.json()


    #get current
    current_data:dict = weather_data.get('current')
    if current_data:
        return current_data.get('temp_c')
    return -1000