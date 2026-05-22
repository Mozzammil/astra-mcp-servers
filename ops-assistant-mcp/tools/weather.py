

def fetch_weather(city: str) -> dict:
    """Mock weather API"""
    fake_weather = {
        "kolkata": {"temp": 32, "condition": "humid 🌫️"},
        "delhi": {"temp": 28, "condition": "dusty 🌪️"},
        "mumbai": {"temp": 30, "condition": "cloudy ☁️"}
    }

    data = fake_weather.get(city.lower(), {
        "temp": 25,
        "condition": "sunny ☀️ (default mock)"
    })

    return {
        "city": city,
        "temperature": data["temp"],
        "condition": data["condition"]
    }