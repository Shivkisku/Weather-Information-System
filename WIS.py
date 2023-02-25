import requests

# Define API key and base URL for OpenWeatherMap API
api_key = 'your-api-key'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Define function to get weather information for a given city
def get_weather(city):
    # Construct API URL for given city and API key
    complete_url = base_url + 'q=' + city + '&appid=' + api_key

    # Send API request and get response
    response = requests.get(complete_url)

    # If API request is successful, parse JSON response and return weather information
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp'] - 273.15, 1), # convert from Kelvin to Celsius
            'description': data['weather'][0]['description']
        }
        return weather
    # If API request fails, return None
    else:
        return None

# Example usage: get weather information for London and print it
london_weather = get_weather('London')
if london_weather:
    print('Weather in', london_weather['city'] + ',', london_weather['country'])
    print('Temperature:', london_weather['temperature'], '°C')
    print('Description:', london_weather['description'])
else:
    print('Failed to get weather information')
