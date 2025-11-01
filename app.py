from flask import Flask, render_template, jsonify
import requests
import os

# --- API Keys (Stored Securely on the Backend) ---
# Your NASA API key from api.data.gov
NASA_API_KEY = '47cUwlR02BEI1ggr6gja9tohe9ygICUPvsB4vt2U'
# Placeholder for the OpenWeatherMap API key
OPENWEATHER_API_KEY = 'bf324b0f9b1439dede4081dd7dcd9d06' 
# -------------------------------------------------



app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main application page."""
    print("Serving the Stellar Tracker application...")
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
        
        # We only return the essential data fields to the frontend
        return jsonify({
            'title': data.get('title', 'Cosmic Event'),
            'explanation': data.get('explanation', 'Data unavailable.'),
            'media_type': data.get('media_type', 'image')
        })
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching APOD data: {e}")
        return jsonify({'error': 'Failed to fetch NASA data.'}), 500

# Note: You could create a similar '/api/weather?lat=X&lon=Y' route 
# to proxy the OpenWeatherMap data and secure that key as well!

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
