from math import sqrt, fabs


# temperature converter F -> C and C -> F
def temp_convert(celsius_to_fahrenheit: float = None, fahrenheit_to_celsius: float = None):
    return (fahrenheit_to_celsius - 32) * 5 / 9 if celsius_to_fahrenheit is None else celsius_to_fahrenheit * 9 / 5 + 32


# real_feel function accepts Celcius temperature, humidity
def heat_index(temperature: float, humidity: float) -> float:
    # convert C to F
    temperature_F = temp_convert(celsius_to_fahrenheit=temperature)

    # calculate heat index
    if temperature_F <= 40:
        heat_i = temperature_F
    else:
        heat_i = -42.379 + 2.04901523*temperature_F + 10.14333127*humidity - 0.22475541*temperature_F*humidity - 0.00683783*(temperature_F**2) - 0.05481717*(humidity**2) + 0.00122874*(temperature_F**2)*humidity + 0.00085282*temperature_F*(humidity**2) - 0.00000199*(temperature_F**2)*(humidity**2)

        # make adjustments
        if humidity < 13 and 80 <= temperature_F <= 112:
            heat_i -= ((13-humidity) / 4) * sqrt(17-fabs(temperature_F - 95) / 17)
        elif humidity > 85 and 80 < temperature_F < 87:
            heat_i += ((humidity - 85) / 10) * ((87 - temperature_F) / 5)
        elif temperature_F < 80:
            heat_i = 0.5 * (temperature_F + 61.0 + ((temperature_F - 68.0) * 1.2) + (humidity * 0.094))

    return temp_convert(fahrenheit_to_celsius=heat_i)


# Wind Chill calculator accepts temperature (C), wind speed (m/s)
def wind_chill(temperature: float, wind_speed: float) -> float:
    # convert m/s to miles/h
    wind_speed_mph = wind_speed * 2.2369362921

    # convert C to F
    temperature_F = temp_convert(celsius_to_fahrenheit=temperature)

    # calculate wind_chill
    result_F = 35.74 + 0.6215 * temperature_F - 35.75 * (wind_speed_mph ** 0.16) + 0.4275 * temperature_F * (wind_speed_mph ** 0.16)

    # convert result from F to C
    return temp_convert(fahrenheit_to_celsius=result_F)


# real feel temperature. pressure effect not included
def real_feel(temperature: float, humidity: float, wind_speed: float) -> float:
    heat_index_value = heat_index(temperature, humidity)

    if temperature < 10 and wind_speed > 1.34112:
        wind_chill_value = wind_chill(temperature, wind_speed)
        return (heat_index_value + wind_chill_value)/2
    else:
        return heat_index_value
