import pygame

pygame.init()

pygame.mixer.music.load("music_file.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass

pygame.mixer.music.stop()
pygame.quit()
