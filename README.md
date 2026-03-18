# SkyCast ☁️

SkyCast is a beautifully designed, modern Python web application that provides live, comprehensive weather data and forecasts using the OpenWeatherMap API.

## ✨ Features
- **Smart Location Search**: Search by city name, zip code, or instantly use your browser's Geolocation.
- **Dynamic Backgrounds**: The entire UI theme shifts fluidly based on the current weather condition (Day, Night, Rain, Snow, etc.).
- **Interactive Live Radar**: An embedded Leaflet.js map automatically centers on your city and overlays live precipitation data.
- **24-Hour Forecast Slider**: A slick, horizontally scrollable view of the short-term temperature trend.
- **Extended Metrics**: View "Feels Like" temperatures, localized Sunrise/Sunset times, Wind Speed, and Humidity.
- **Favorite Locations**: Star your most-searched cities to save them to your browser's LocalStorage for 1-click access.

## 🛠️ Technology Stack
- **Backend**: Python, Flask, Requests
- **Frontend**: HTML5, Tailwind CSS (via CDN), JavaScript (Vanilla)
- **APIs & Libraries**: OpenWeatherMap API, Leaflet.js, FontAwesome

## 🚀 Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SkyCast.git
   cd SkyCast
   ```

2. **Install requirements**
   Ensure you have Python installed, then run:
   ```bash
   pip install flask requests python-dotenv
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```env
   API_KEY=your_openweathermap_api_key_here
   ```

4. **Run the App**
   ```bash
   python app.py
   ```
   Open `http://localhost:5000` in your browser!

## 📸 Screenshots
*(Add screenshots of your amazing UI here!)*

## 📄 License
This project is open-source and available under the MIT License.
