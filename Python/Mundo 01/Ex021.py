'''
 - Programa: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
import pygame
# Processamento:
pygame.init()
pygame.mixer.music.load('Audio B.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Fim.