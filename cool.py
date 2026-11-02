import pygame
pygame.init()

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
    waitforaction("unpause", False, unpause)

def play(filename):
    pygame.mixer.music.load(f"{filename}.mp3")
    pygame.mixer.music.play()
    waitforaction("pause", True, pause)


playlist = ["weathergirl ft. Eleanor Forte 4", "Audio"]



while True:
    for i in range(len(playlist)):
        if i != len(playlist):
            queue(playlist[i+1])
            play(playlist[i])
        elif i == len(playlist):
            queue(0)
            play(playlist[i])

