from flask import Flask, render_template, jsonify, request
import requests
import os

# --- API Keys (Stored Securely on the Backend) ---
# Your NASA API key from api.data.gov
NASA_API_KEY = '47cUwlR02BEI1ggr6gja9tohe9ygICUPvsB4vt2U'
# OpenWeatherMap API key
OPENWEATHER_API_KEY = 'bf324b0f9b1439dede4081dd7dcd9d06'
# -------------------------------------------------


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main application page."""
    print("Serving the Stellar Tracker application...")
    # NOTE: You would need an 'index.html' template file in a 'templates' folder
    # for this function to work in a real Flask environment.
    return render_template('index.html')


@app.route('/api/apod')
def get_apod():
    """
    Proxies the request to NASA's Astronomy Picture of the Day (APOD) API.
    
    This keeps the NASA_API_KEY secure on the server.
    """
    NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': NASA_API_KEY}
    
    try:
        response = requests.get(NASA_APOD_URL, params=params)
        response.raise_for_status() # Raises an HTTPError if the status is 4xx or 5xx
        
        data = response.json()
        
        # We return the essential data fields to the frontend, including the URL
        return jsonify({
            'title': data.get('title', 'Cosmic Event'),
            'explanation': data.get('explanation', 'Data unavailable.'),
            'media_type': data.get('media_type', 'image'),
            'url': data.get('url') # Crucial for displaying the image/video
        })
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching APOD data: {e}")
        return jsonify({'error': 'Failed to fetch NASA data.'}), 500

@app.route('/api/weather')
def get_weather():
    """
    Proxies the request to the OpenWeatherMap API using latitude and longitude.
    
    Expects 'lat' and 'lon' query parameters.
    """
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    if not latitude or not longitude:
        return jsonify({'error': 'Missing latitude (lat) or longitude (lon) parameter for weather data.'}), 400

    OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric' # You can change this to 'imperial' if you prefer Fahrenheit
    }

    try:
        response = requests.get(OPENWEATHER_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract relevant fields for the frontend
        weather_data = {
            'city': data.get('name', 'Unknown Location'),
            'temperature': data.get('main', {}).get('temp'),
            'description': data.get('weather', [{}])[0].get('description'),
            'icon': data.get('weather', [{}])[0].get('icon'),
            'wind_speed': data.get('wind', {}).get('speed')
        }
        
        return jsonify(weather_data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OpenWeatherMap data: {e}")
        return jsonify({'error': 'Failed to fetch weather data.'}), 500


if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
