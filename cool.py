import pygame
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
pygame.mixer.init()


while True:
    Warning("Warning!")

playlist = [
    {
        "audio": "Audio",
        "image": "images",
    },
    {
        "audio": "weathergirl ft. Eleanor Forte 4",
        "image": "calude",
    },
    {
        "audio": "I LIKE LOUD THINGS",
        "image": "image02"
    },
    {
        "audio": "Obelisk of SOOO retro",
        "image": "image02"
    }
]

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("audio player")
        self.root.geometry("500x500")

        self.index = 0
        self.paused = False

        self.setui()
        self.play()

        self.checkaudiostatus()

    def setui(self):
        frame = ttk.Frame(self.root)
        frame.pack()
        self.title = ttk.Label(frame, text="")
        self.title.pack()
        self.img = ttk.Label(frame)
        self.img.pack()
        controls = ttk.Frame(frame)
        controls.pack()
        self.previous = ttk.Button(controls, text="previous", command=self.previous_button)
        self.previous.pack()
        self.next = ttk.Button(controls, text="next", command=self.next_button)
        self.next.pack()
        self.pause = ttk.Button(controls, text="pause", command = self.play_pause)
        self.pause.pack()

    def play(self):
        song = playlist[self.index]
        self.title.config(text=song["audio"])

        img = Image.open(f"{song['image']}.jpg")
        img = img.resize((250, 250), Image.Resampling.LANCZOS)
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

    def checkaudiostatus(self):
        if not pygame.mixer.music.get_busy() and not self.paused:
            self.next_button()
        self.root.after(1000, self.checkaudiostatus)


root = tk.Tk()
app = gui(root)
root.mainloop()

