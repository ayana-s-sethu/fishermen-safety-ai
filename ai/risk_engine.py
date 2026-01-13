def analyze_risk(weather: dict):
    wind = weather["wind_speed_kmh"]

    if wind > 25:
        return {
            "risk_level": "HIGH",
            "safe_till": "Not safe",
            "advice": "Do NOT go fishing",
            "zone": "Stay ashore"
        }

    elif 15 <= wind <= 25:
        return {
            "risk_level": "MODERATE",
            "safe_till": "10:00 AM",
            "advice": "Fish near shore and return early",
            "zone": "Up to 5 km"
        }

    else:
        return {
            "risk_level": "LOW",
            "safe_till": "All day",
            "advice": "Safe for fishing",
            "zone": "Up to 10 km"
        }
