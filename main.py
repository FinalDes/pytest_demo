def get_weather(temp):
    THRESHOLD_TEMP_CELSIUS = 20
    if temp > THRESHOLD_TEMP_CELSIUS:
        return "hot"
    else:
        return "cold"
