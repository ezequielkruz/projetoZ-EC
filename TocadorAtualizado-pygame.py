import pygame

pygame.init()
pygame.mixer.music.load('300 Violin Orchestra.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()