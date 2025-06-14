# WeatherMoodify 🎶🌤️

**WeatherMoodify** is an intelligent playlist generator that combines your current mood 😊😢😎 with real-time weather data 🌞🌧️ to deliver personalized music recommendations 🎧. It leverages advanced web scraping 🕸️, sentiment analysis 🧠, and an intuitive graphical interface 🖥️ to create a unique and immersive music experience without relying on external APIs.

---

## Features ✨

- **Live Weather Scraping** 🌍  
  Extracts current weather conditions by scraping Google Search results dynamically, ensuring up-to-date contextual data.

- **Advanced Mood Detection** 🤖  
  Uses NLTK's sentiment analysis and emoji mapping to interpret your mood from text or emoji input.

- **Expanded Playlist Database** 🎼  
  Rich, customizable playlists matched to combinations of mood and weather conditions.

- **Graphical User Interface** 🖱️  
  User-friendly Tkinter-based GUI for seamless interaction including city and mood input, playlist display, clipboard copying, and file export.

- **Data Persistence** 💾  
  Local JSON-based storage of playlists, enabling customization and future expansion.

- **Playlist Export & Clipboard Support** 📋📁  
  Export your personalized playlist to a text file or copy it directly to your clipboard with a single click.

---

## Installation 🛠️

Make sure you have Python 3.7 or newer installed.

Install required packages via pip:

```bash
pip install requests beautifulsoup4 nltk pyperclip
Usage 🚀
Clone this repository:

git clone https://github.com/yourusername/WeatherMoodify.git
cd WeatherMoodify

Run the GUI application:
python main_gui.py

Enter your city 🏙️ and mood (text or emoji) 😊, then click Generate Playlist.

View your personalized playlist 🎶, then optionally copy it to your clipboard 📋 or export it as a file 📂.

Project Structure 🗂️
main_gui.py — The main Tkinter GUI application.

mood_detector.py — Detects user mood using NLP and emoji mapping.

weather_scraper.py — Scrapes weather data from Google Search results.

playlist_manager.py — Manages playlists, exporting, and data persistence.

playlist_db.json — (Optional) JSON file for storing custom playlists and preferences.

Customization 🎨
Add your own playlists by modifying playlist_db.json or updating the DEFAULT_PLAYLISTS in playlist_manager.py.

Expand mood and weather categories for more nuanced recommendations.

Troubleshooting 🛠️
Weather data not loading? 🌧️
Google may have changed their page layout. Check the weather_scraper.py logic or fallback to cached data.

NLTK data missing? 📚
Run Python shell and execute:

import nltk
nltk.download('vader_lexicon')

Clipboard not working? 📋❌
Ensure pyperclip supports your OS clipboard backend.

Future Enhancements 🚧
Integrate with music streaming APIs for direct playback 🎵▶️.

Add AI-driven personalized music recommendations based on listening history 🤖🎧.

Create a mobile app version using Kivy or React Native 📱.

User account system with cloud sync ☁️🔄.

