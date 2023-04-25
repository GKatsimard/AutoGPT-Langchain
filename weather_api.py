import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data['weather'][0]['description']