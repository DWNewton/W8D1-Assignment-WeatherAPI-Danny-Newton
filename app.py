from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "6cc5dfa562904125992214314240107"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/weather', methods=['GET'])

# endpoint to get weather info
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not specified"}), 400
    
    try:
        response = requests.get(WEATHER_API_URL, params={"key": API_KEY, "q": city})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error fetching data from WeatherAPI", "details": str(e)}), 500

    data = response.json()

    if "error" in data:
        return jsonify({"error": "Unknown city"}), 404

# Sourced from WeatherAPI format info
    weather_info = {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "wind_speed": data["current"]["wind_mph"]
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)