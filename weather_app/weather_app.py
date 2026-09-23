
import json
from urllib.parse import quote
from urllib.request import urlopen


def get_city_coordinates(city):

    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        "?name=" + quote(city)
        + "&count=1&language=en&format=json"
    )

    with urlopen(url) as response:
        data = json.load(response)

    if "results" not in data:
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=" + str(latitude)
        + "&longitude=" + str(longitude)
        + "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,weather_code,wind_speed_10m"
        "&timezone=auto"
    )

    with urlopen(url) as response:
        data = json.load(response)

    return data


def get_weather_description(weather_code):

    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    return weather_conditions.get(
        weather_code,
        "Unknown weather condition"
    )


print("================================")
print("       WEATHER APP")
print("================================")

city = input("Enter city name: ")

try:

    location = get_city_coordinates(city)

    if location is None:
        print("City not found. Please try again.")

    else:

        weather_data = get_weather(
            location["latitude"],
            location["longitude"]
        )

        current_weather = weather_data["current"]

        temperature = current_weather["temperature_2m"]
        humidity = current_weather["relative_humidity_2m"]
        feels_like = current_weather["apparent_temperature"]
        weather_code = current_weather["weather_code"]
        wind_speed = current_weather["wind_speed_10m"]

        weather_description = get_weather_description(
            weather_code
        )

        print()
        print("Weather Information")
        print("----------------------------")
        print("City:", location["name"])
        print("Country:", location["country"])
        print("Temperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")
        print("Condition:", weather_description)

except Exception as error:

    print("Something went wrong.")
    print("Error:", error)
