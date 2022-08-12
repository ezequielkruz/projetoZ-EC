print('\033[1;33mFaça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\033[m')
print('\033[1;31m')
print('8'*12, 'Desafio 21', '8'*12)
print('\033[m')
#import ossaudiodev
#ossaudiodev.open(device='3 door down')'''

# Guanabara

import pygame

pygame.init()
pygame.mixer.music.load('3 Doors Down.mp3')
pygame.mixer.music.play()
input()
