import pygame
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
pygame.mixer.init()

playlist = [
    {
        "audio": "Bark Fart Sound Effect",
        "image": "what",
    },
    {
        "audio": "Audio",
        "image": "images",
    },
    {
        "audio": "weathergirl ft. Eleanor Forte 4",
        "image": "calude",
    }
]

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("gui")
        self.root.geometry("500x500")

        self.index = 0
        self.paused = False

        self.setui()
        self.play()

        self.check_audio_status()

    def setui(self):
        frame = ttk.Frame(self.root)
        self.title = ttk.Label(frame, text="")
        self.img = ttk.Label(frame)
        controls = ttk.Frame(frame)
        self.previous = ttk.Button(controls, text="previous", command=self.previous_button)
        self.next = ttk.Button(controls, text="next", command=self.next_button)
        self.pause = ttk.Button(controls, text="pause", command = self.play_pause)

    def play(self):
        song = playlist[self.index]
        self.title.config(text=song["audio"])

        img = Image.open(f"{song['image']}.jpg")
        self.photo = ImageTk.PhotoImage(img)
        self.img.config(image=self.photo)

        pygame.mixer.music.load(f"{song['audio']}.mp3")
        pygame.mixer.music.play()
        self.paused = False
        self.pause.config(text="Pause")

    def play_pause(self):
        if self.paused == True:
            pygame.mixer.music.unpause()
            self.paused = False
            self.pause.config(text="Pause")
        else:
            pygame.mixer.music.pause()
            self.paused = True
            self.pause.config(text="Play")
  
    def next_button(self):
        self.index = (self.index + 1) % len(playlist)
        self.play()

    def previous_button(self):
        self.index = (self.index - 1) % len(playlist)
        self.play()

    def check_audio_status(self):
        if not pygame.mixer.music.get_busy() and not self.paused:
            self.next_button()
        self.root.after(1000, self.check_audio_status)


root = tk.Tk()
app = gui(root)
root.mainloop()