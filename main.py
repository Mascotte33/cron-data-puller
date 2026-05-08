import requests
from dotenv import load_dotenv
import os 

if os.path.exists('.env'):
    load_dotenv('.env')

API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("WEATHER_API_KEY environment is not set up")
weather_url = 'http://api.weatherapi.com/v1/current.json?key='  

def get_weather_data(cities):
    cities_data_list = []
    try:
        for city in cities:
            response = requests.get(f'{weather_url}{API_KEY}&q={city}').json()
            cities_data_list.append(response)
        return cities_data_list
    
    except Exception as e:
        print(f'Getting weather information failed. \n Exception: {e}')
 
def generate_html(cities_data_list):
    if not cities_data_list:
        print('No data to generate HTML')
        return
    try:
        cards = []

        for city in cities_data_list:            
            card = f"""
                <div class="weather-card">
                    <div class="city">{city['location']['name']}</div>
                    <div class="temp">{city['current']['temp_c']}°C</div>
                    <div class="condition">{city['current']['condition']['text']}</div>
                    <div class="last_updated">{city['current']['last_updated']}</div>
                </div>
            """
            cards.append(card)
        
        with open('template.html', 'r') as file:
            filedata = file.read()
            filedata = filedata.replace('WEATHER_CARDS', '\n'.join(cards))
        with open('index.html', 'w') as file:
            file.write(filedata)

    except Exception as e: 
        print(f'Generating HTML failed. \n Exception: {e}')


if __name__ == "__main__":   
    cities = ['Cracow', 'Warsaw', 'Poznan', 'Gdansk', 'Wroclaw']
    cities_data_list = get_weather_data(cities)
    generate_html(cities_data_list)

