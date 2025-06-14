import tkinter as tk
from tkinter import messagebox, filedialog
from mood_detector import detect_mood
from weather_scraper import scrape_weather
from playlist_manager import load_playlists, get_playlist, export_playlist, copy_to_clipboard

class MoodMixApp:
    def __init__(self, root):
        self.root = root
        root.title("MoodMix Playlist Generator")

        self.playlists = load_playlists()

        # UI Elements
        tk.Label(root, text="Enter your city:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.city_entry = tk.Entry(root)
        self.city_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter your mood (text or emoji):").grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.mood_entry = tk.Entry(root)
        self.mood_entry.grid(row=1, column=1, padx=10, pady=5)

        self.generate_btn = tk.Button(root, text="Generate Playlist", command=self.generate_playlist)
        self.generate_btn.grid(row=2, column=0, columnspan=2, pady=10)

        self.playlist_box = tk.Listbox(root, width=50, height=10)
        self.playlist_box.grid(row=3, column=0, columnspan=2, padx=10)

        self.copy_btn = tk.Button(root, text="Copy to Clipboard", command=self.copy_playlist)
        self.copy_btn.grid(row=4, column=0, pady=10)

        self.export_btn = tk.Button(root, text="Export to File", command=self.export_playlist)
        self.export_btn.grid(row=4, column=1, pady=10)

    def generate_playlist(self):
        city = self.city_entry.get().strip()
        mood_input = self.mood_entry.get().strip()
        if not city or not mood_input:
            messagebox.showwarning("Input Error", "Please enter both city and mood.")
            return

        mood = detect_mood(mood_input)
        weather = scrape_weather(city)

        if not weather:
            weather = 'clear'  # fallback

        playlist = get_playlist(mood, weather, self.playlists)

        self.playlist_box.delete(0, tk.END)
        for song in playlist:
            self.playlist_box.insert(tk.END, song)

        messagebox.showinfo("Playlist Generated", f"Detected mood: {mood}\nWeather: {weather}")

    def copy_playlist(self):
        songs = self.playlist_box.get(0, tk.END)
        if songs:
            copy_to_clipboard(songs)
            messagebox.showinfo("Copied", "Playlist copied to clipboard.")
        else:
            messagebox.showwarning("No Playlist", "Generate a playlist first.")

    def export_playlist(self):
        songs = self.playlist_box.get(0, tk.END)
        if not songs:
            messagebox.showwarning("No Playlist", "Generate a playlist first.")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if filename:
            export_playlist(songs, filename)
            messagebox.showinfo("Exported", f"Playlist saved to {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodMixApp(root)
    root.mainloop()
