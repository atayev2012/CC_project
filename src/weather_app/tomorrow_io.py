from config import WEATHER_API_KEY, WEATHER_URL
from src.weather_app.real_feel import real_feel
from requests import post

# Fields:
# temperature -> real temperature (Celcius [-90, 60])
# temperatureApparent -> real feel (Celcius [-90, 60])
# humidity -> humidity (%)
# windSpeed -> wind speed (m/s)
# pressureSurfaceLevel -> atmospheric pressure (hPa/inHg)
# rainIntensity -> rain per period (mm/hr)
# snowIntensity -> snow (mm/hr)

# URL adress for API requests
URL = f"{WEATHER_URL}?apikey={WEATHER_API_KEY}"


# request weather for a specific location (latitude & longitude)
def request_weather(lat: float, lon: float, forecast_hours: int = 24) -> list:
    result = []
    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "content-type": "application/json"
    }

    params = {
        "location": f"{lat}, {lon}",
        "fields": ["temperature", "humidity", "windSpeed"],
        "units": "metric",
        "timesteps": ["1h"],
        "startTime": "now",
        "endTime": f"nowPlus{forecast_hours}h",
        "timezone": "Europe/Volgograd"
    }

    response = post(URL, json=params, headers=headers)
    data = response.json()

    for item in data["data"]["timelines"][0]["intervals"]:
        result.append({
            "date": item["startTime"].split("T")[0],
            "time": item["startTime"].split("T")[1][:8],
            "temperature": item["values"]["temperature"],
            "temperatureRealFeel": real_feel(item["values"]["temperature"], item["values"]["humidity"], item["values"]["windSpeed"])
        })

    return result
