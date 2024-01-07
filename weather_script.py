import requests
#get your API KEY and put in a variable 
api_key = "8fa8290df4ad00d21c8612fa8ff53f30"

#provide a function that recieves an input and then checks for the weather conditions for the input
def get_Weather(city):
    #get url to request from.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    #get infro from the url
    response = requests.get(url)
    if response.status_code == 200:
            data = response.json()
            #extract weather data from response
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data ['wind']['speed']
            #display weather information to the user 
            print(f"Weather in {city}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Wind speed: {wind_speed}")
    else:
            print('Failed to fetch weather detail, please check the city name or API key. Thank you.')
#main program loop
while True:
    city = input('Enter your city name(or q to quit):')
    if city.lower() == 'q':
        break
    get_Weather(city)
print('Goodbye')