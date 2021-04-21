'''Faça um programa em Python que abra
 e reproduza o áudio de um arquivo MP3.'''
'''import pygame
pygame.init()
pygame.mixer.music.load('EX-21remix.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''Explicação do primerio erro: https://pt.stackoverflow.com/questions/288050/m%c3%basica-n%c3%a3o-toca'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('EX-21seujorge.mp3')
pygame.mixer.music.play()
x = input('Digite algo quando quiser parar a música: ')