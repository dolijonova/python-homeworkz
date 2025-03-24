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
        print(f"Failed to get weather data. Status code: {response.status_code}")

api_key = "your_api_key"
city = "Chirchik"
fetch_weather_data(api_key, city)


print("Task 2")
import requests
import random

def get_movie(api_key,genre_id):
    url=f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"

    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        movies=data['results']
        if movies:
            random_movie=random.choice(movies)
            return random_movie
        else:
            return None
    else:
        print("Movie can not be found")
        return None
    
def recommendMovie(api_key):
    genres={
        "Horror":12,
        "Romance":11,
        "Comedy":13
    }
    genre=input().capitalize()
    if genre in genres:
        genre_id=genres[genre]
        movie=get_movie(api_key,genre_id)
        if movie:
            print(f"{movie['title']} is recommended for you ")
        else:
            print("There was not any movie suitable for you")
    else:
        print("The genre is not present on us")

api_key="your_api_key"
recommendMovie(api_key)