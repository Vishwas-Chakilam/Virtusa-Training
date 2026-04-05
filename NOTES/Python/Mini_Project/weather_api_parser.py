import json
import urllib.request
import urllib.error

def fetch_weather(city_code="London"):
    # Using a dummy API format to simulate external fetch gracefully
    url = f"https://api.weather.gov/gridpoints/TOP/31,80/forecast" # Public sample API
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            periods = data['properties']['periods']
            print(f"--- Forecast ---")
            for prop in periods[:3]:
                print(f"{prop['name']}: {prop['temperature']}F, {prop['shortForecast']}")
    except urllib.error.URLError as e:
        print(f"Network error or invalid API structure: {e}")

if __name__ == "__main__":
    fetch_weather()