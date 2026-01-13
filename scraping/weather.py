# scraping/weather.py

def get_weather_by_latlon(lat: float = 0, lon: float = 0):
    """
    Offline-safe dummy weather
    """
    return {
        "wind_speed": 18,      # km/h
        "wave_height": 1.6,    # meters
        "rain": False,
        "visibility": "Good"
    }
