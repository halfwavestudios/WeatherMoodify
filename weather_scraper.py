import requests
from bs4 import BeautifulSoup

def scrape_weather(city):
    query = f"weather {city}"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    weather_div = soup.find("div", attrs={"id": "wob_dc"})
    if weather_div:
        weather = weather_div.text.lower()
        if 'rain' in weather or 'drizzle' in weather or 'showers' in weather:
            return 'rain'
        elif 'cloud' in weather or 'overcast' in weather:
            return 'clouds'
        elif 'sun' in weather or 'clear' in weather or 'sunny' in weather:
            return 'clear'
        elif 'snow' in weather:
            return 'snow'
        else:
            return 'clear'
    return None
