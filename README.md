# 🌌 Stellarium Geolocation Atlas 🛰️

> A dynamic web application that visualizes a user's real-time geographic position as an animated, pulsing star on a deep-space map backdrop.
---

### 🌐 Live Demo
You can view the fully deployed, live version of this project here:
➡️ **[View Live Demo]** ([https://github.com/FudeezValo/stellarium-geolocation-atlas])

### ✨ Key Features

* **Real-Time Geolocation:** Uses the HTML5 `navigator.geolocation` API to fetch the user's latitude and longitude on demand.
* **"Stellarium" Styling:** The map utilizes the **MapTiler DataViz Dark** tile layer via Leaflet.js to mimic the high-contrast aesthetic of an astronomical chart.
* **Animated Marker:** The user's position is marked by a custom **CSS Keyframe Animation** that creates a continuous, glowing pulse effect (a "star pulse").
* **Clear Feedback:** Provides immediate status updates (Locating, Success, Permission Denied, Error) to the user.
* **Responsive UI:** Built with **Tailwind CSS** for a clean, modern, and mobile-friendly interface.

* ### 🛠️ Tech Stack & Dependencies

* **HTML5:** Structure
* **JavaScript (Vanilla):** Client-side logic and Geolocation API integration
* **CSS / Tailwind CSS:** Styling and responsiveness
* **Leaflet.js:** Open-source library for interactive maps
* **MapTiler:** Tile provider for the dark, high-contrast map aesthetic (API Key Required)

* ### 🚀 Local Setup

To run this project locally, clone the repository and open the `index.html` file in your browser.

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:FudeezValo/stellarium-geolocation-atlas.git
    cd stellarium-geolocation-atlas
    ```
2.  **Add MapTiler API Key:**
    * The `index.html` file requires a valid MapTiler API key (the one you provided) to load the map tiles. It is currently hardcoded in the script, but for larger projects, you should use environment variables.
3.  **Run:** Open `index.html` directly in your web browser. You will need to click the "Locate User Position" button and grant location permission.
