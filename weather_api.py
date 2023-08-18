import requests

from config import OWM_Endpoint, api_password


# Function that gets is it raining or not on current latitude/longitude combination
def give_forecast(lat, long):

    parameters = {
        "lat": lat,
        "lon": long,
        "exclude": "current,minutely,daily",
        "appid": api_password,
    }

    response = requests.get(url=OWM_Endpoint, params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    weather_slice = weather_data["hourly"][:12]
    will_rain = False

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    if will_rain:
        return "UMBRELLA!!!"
    else:
        return "not rain"
