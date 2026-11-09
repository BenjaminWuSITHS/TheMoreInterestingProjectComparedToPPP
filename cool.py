import pygame

from PIL import Image
img = Image.open("calude.jpg")

img.show()

pygame.init()
playlist = [
    {
        "audio": "Bark Fart Sound Effect",
        "image": "",
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

playlist = ["Bark Fart Sound Effect","Audio", "weathergirl ft. Eleanor Forte 4"]

def showimage():
    print("")


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
            queue(playlist[i+1])
            play(playlist[i])
        elif i+1 == len(playlist):
            queue(playlist[0])
            play(playlist[i])

