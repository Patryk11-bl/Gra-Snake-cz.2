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

    def sprawdz_kolizje(self):
        for segment in self.segmnety:
            if self.rect.topleft == segment.pozycja.topleft:
                return True
        if self.rect.top < 0 or self.rect.top >=608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True
        return False

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

        for i in range(len(self.segmnety)):
            if i ==0:
                self.segmnety[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmnety[i].przesun(self.segmnety[i-1].ostatnia_pozycja)
        
        if self.dodaj_segement:
            nowy_segment = Segment()

            nowa_pozycja = None
            if len(self.segmnety) >0:
                nowa_pozycja = copy.deepcopy(self.segmnety[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
            nowy_segment.pozycja = nowa_pozycja
            self.segmnety.append(nowy_segment)
            self.dodaj_segement = False
    def rysuj_segmenty(self, ekran):
        for segment in self.segmnety:
            ekran.blit(segment.obraz, segment.pozycja)

    def jedz_jablko(self):
        self.dodaj_segement = True
