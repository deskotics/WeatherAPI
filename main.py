import requests

city_name = 'Seattle'.replace(" ", "%20")
api_key = '' # your api key goes here

def get_weather(city, key):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

  response = requests.get(url).json() 
  temp = response['main']['temp']
  
  temp = convert_temp(temp)
  print(temp)
  
  feels_like = response['main']['feels_like']
  feels_like = convert_temp(feels_like)



def convert_temp(temp): # converts to F
  return (temp*1.8) - 459.67


get_weather(city_name, api_key)
