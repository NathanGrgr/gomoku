import math
import cmath
from tkinter import *
VIDE = 0
OCCUPE = 1
TAILLE_GRILLE = 100

class Canvas_gomoku(Canvas):
    def __init__(self, fenetre):
        super().__init__(fenetre, width=500, height=500, bg='white')
        self.pack()

    def dessine_case(self, x_grille, y_grille, couleur):
        taille = self.taille_case
        x, y = x_grille*taille, y_grille*taille
        x_prime=x+taille
        y_prime=y+taille
        self.create_rectangle(x,y,x_prime,y_prime,fill=couleur,outline=couleur)

if __name__ == "__main__":
    fenetre_principale = Tk()
    fenetre_principale.title("gomoku")
    fenetre_principale.geometry("600x600")

    grille = [[VIDE for _ in range(100)] for _ in range(100)]

    canvas = Canvas_gomoku(fenetre_principale)