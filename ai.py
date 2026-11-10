import os
import pygame
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
pygame.mixer.init()

playlist = [
    {"audio": "Bark Fart Sound Effect", 
     "image": "what"},
    {"audio": "Audio",
      "image": "images"},
    {"audio": "weathergirl ft. Eleanor Forte 4",
      "image": "calude"}
]

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("TTK Audio Player")
        self.root.geometry("400x500")
        
        self.current_index = 0
        self.is_paused = False
        
        self.setup_ui()
        self.play_current()
        
        self.check_audio_status()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.title_label = ttk.Label(main_frame, text="", font=("Arial", 14, "bold"), wraplength=350)
        self.title_label.pack(pady=10)

        self.img_label = ttk.Label(main_frame)
        self.img_label.pack(pady=20)
        
        controls_frame = ttk.Frame(main_frame)
        controls_frame.pack(pady=20)
        
        self.prev_btn = ttk.Button(controls_frame, text="Previous", command=self.prev_track)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.play_pause_btn = ttk.Button(controls_frame, text="Pause", command=self.toggle_play_pause)
        self.play_pause_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(controls_frame, text="Next", command=self.next_track)
        self.next_btn.pack(side=tk.LEFT, padx=5)

    def play_current(self):
        track = playlist[self.current_index]
        self.title_label.config(text=track["audio"])
        
        # Update Image inside the GUI instead of launching an external viewer
        img_path = f"{track['image']}.jpg"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((250, 250), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.photo)
        else:
            self.img_label.config(image="", text="[No Image Found]")

        # Play audio file
        audio_path = f"{track['audio']}.mp3"
        if os.path.exists(audio_path):
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            self.is_paused = False
            self.play_pause_btn.config(text="Pause")
        else:
            self.title_label.config(text=f"{track['audio']} not found")

    def toggle_play_pause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.play_pause_btn.config(text="Pause")
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.play_pause_btn.config(text="Play")

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(playlist)
        self.play_current()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(playlist)
        self.play_current()

    def check_audio_status(self):
        if not pygame.mixer.music.get_busy() and not self.is_paused:
            self.next_track()
        self.root.after(1000, self.check_audio_status)


root = tk.Tk()
app = AudioPlayer(root)
root.mainloop()
