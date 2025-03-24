import requests

def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    
    response = requests.get(url)
    
  
    if response.status_code == 200:
        data = response.json()
        
       
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")

api_key = "your_api_key"
city = "Chirchik"
fetch_weather_data(api_key, city)