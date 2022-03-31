# import playsound
#
# playsound.playsound('c:/Users/Eduardo/Music/Vivaldi_The Four Seasons_Spring-Allegro.mp3', True)  # "a musica tem
                                                                                                    # que estar nesse diretório e a contra-barra \ tem que ser trocada para barra /

import pygame
# from pygame import mixer
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('C:/Users/Eduardo/Music/Vivaldi_The Four_Seasons_Spring-Allegro.mp3')  # "a musica tem que estar nesse diretório
pygame.mixer.music.play()                                                                      # e a contra-barra \ tem que ser trocada para barra /
input()
pygame.event.wait()
