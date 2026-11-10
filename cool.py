import pygame

from PIL import Image


pygame.init()
playlist = [
    {
        "audio": "Bark Fart Sound Effect",
        "image": "what",
    },
    {
        "audio": "Bark Fart Sound Effect",
        "image": "images",
    },
    {
        "audio": "Bark Fart Sound Effect",
        "image": "calude",
    }
]


def showimage(img):
    Image.open(f"{img}.jpg").show()

def queue(filename):
    pygame.mixer.music.queue(f"{filename}.mp3")

def waitforaction(action_needed, bool, returning):
    while pygame.mixer.music.get_busy() == bool:
        action = input()
        if action == action_needed:
            returning()
def unpause():
    pygame.mixer.music.unpause()
    waitforaction("pause", True, pause)

def pause():
    pygame.mixer.music.pause()
    waitforaction("play", False, unpause)

def play(filename):
    pygame.mixer.music.load(f"{filename}.mp3")
    pygame.mixer.music.play()
    waitforaction("pause", True, pause)


while True:
    for i in range(len(playlist)):
        if i+1 != len(playlist):
            queue(playlist[i+1]["audio"])
            showimage(playlist[i]["image"])
            play(playlist[i]["audio"])
            print("loop playlist?")
        elif i+1 == len(playlist):
            queue(playlist[0]["audio"])
            showimage(playlist[i]["image"])
            play(playlist[i]["audio"])
            print("continue playlist?")

