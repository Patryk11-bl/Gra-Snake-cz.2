import pygame
from Kierunek import Kierunek
import copy
from Segment import Segment

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        #oryginalny obraz glowy
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        #obraz pomocniczny, bedzie sie on zmienial przy zmienie kierunku gracza
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        #wspolrzednie glowy
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))
        #zmienne odpowiedzialne za kierunek, oraz nowy wyznaczony kierunek
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA
        self.ostatnia_pozycja = self.rect
        self.dodaj_segement = False
        self.segmnety = []


    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True
        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if zmiana_mozliwa: 
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))

        
        self.ostatnia_pozycja = copy.deepcopy(self.rect)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)
