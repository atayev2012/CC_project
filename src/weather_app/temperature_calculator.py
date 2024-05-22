# from src.weather_app.tomorrow_io import request_weather
from datetime import datetime


# calculate daily temperature with hourly weater data
def daily_temperature(temperature_data: list) -> dict:
    # if temperature_data is empty return None result
    if not temperature_data:
        return {"temperature": None, "real_feel": None}

    temp_list = [item["temperature"] for item in temperature_data]
    temp_real_feel_list = [item["temperatureRealFeel"] for item in temperature_data] 
    
    temperature = (max(temp_list) + min(temp_list))/2
    temperature_real_feel = (max(temp_real_feel_list) + min(temp_real_feel_list))/2

    return {"current_temperature": round(temp_list[0], 3),"average_temperature": round(temperature, 3), "average_real_feel": round(temperature_real_feel, 3)}    
