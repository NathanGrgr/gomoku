from tkinter import *
import math
from random import randint



FACT=30
LINES=15
WIDTH=FACT*(LINES-1)
OFFSET=10
RADIUS=10
win_condition=5
TAILLE_GRILLE=15


class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.taille_case = int(self['width']) // TAILLE_GRILLE
        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img

    def click(self, x, y):
        xr=OFFSET+math.floor((x+FACT/2-OFFSET)/FACT)*FACT
        yr=OFFSET+math.floor((y+FACT/2-OFFSET)/FACT)*FACT
        print("click", x, y,"->",xr,yr)
        area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="black")

    def bot(self):
        x_grille=randint(0,15)
        y_grille=randint(0,15)
        taille = self.taille_case
        x, y = x_grille*taille, y_grille*taille
        x_prime=x+taille
        y_prime=y+taille
        print("test")
        area_draw.create_oval(x,y,x_prime,y_prime,fill="red")


"""
self.taille_case = int(self['width']) // TAILLE_GRILLE
taille = self.taille_case
x, y = x_grille*taille, y_grille*taille
x_prime=x+taille
y_prime=y+taille
"""


class Gomoku:
    def __init__(self):
        self.L=[[None for i in range(15)] for i in range(15)]


    def filling(self,i,j,pawn):
        self.L[i][j]=pawn
        return (self.L[i][j])


    def condition_verticale(self,pawn):
        for i in range(len(self.L)):
            counter=0
            for j in range(len(self.L)):
                if self.L[i][j]==pawn:
                    counter+=1
                    for x in range(4):
                        if self.L[i][j+counter]==pawn:
                            counter+=1
                    if counter==win_condition:
                        return("verticale")
                    else:
                        return("non verticale")


    def condition_horizontal(self,pawn):
        for i in range(len(self.L)):
            L_coordonates=[]
            counter=0
            for j in range(len(self.L)):
                if self.L[i][j]==pawn:
                    tuple=(i+counter,j-counter)
                    L_coordonates.append(tuple)
                    counter+=1
                    for x in range(4):
                        if self.L[i+counter][j]==pawn:
                            tuple=(i+counter,j-counter)
                            L_coordonates.append(tuple)
                            counter+=1
                    if counter==win_condition:
                        print("horizontale")
                        return(L_coordonates)
                    else:
                        return("non horizontale")


    def condition_diagonal(self,pawn):
        for i in range(len(self.L)):
            counter=0
            for j in range(len(self.L)):
                if self.L[i][j]==pawn:
                    counter+=1
                    for x in range(4):
                        if self.L[i+counter][j+counter]==pawn:
                            counter+=1
                    if counter==win_condition:
                        return("diagonale 1")
                    else:
                        for i in range(len(self.L)):
                            counter=0
                            L_coordonates=[]
                            for j in range(len(self.L)):
                                if self.L[i][j]==pawn:
                                    tuple=(i+counter,j-counter)
                                    L_coordonates.append(tuple)
                                    counter+=1
                                    for x in range(4):
                                        
                                        if self.L[i+counter][j-counter]==pawn:
                                            if j-counter<0:
                                                return("no diag")
                                            tuple=(i+counter,j-counter)
                                            L_coordonates.append(tuple)
                                            counter+=1
                                    if counter==win_condition:
                                        print("diag 2")
                                        return(L_coordonates)
                                    else:
                                        return("no diag")

#i nombre de ligne
#j nombre d'éléments à l'intérieur de la ligne

#00 11 22 
#4,0 3,1 2,2 1,3 0,4


if __name__=="__main__":
    black=Gomoku()
    white=Gomoku()
    black.filling(4,0,"black")
    black.filling(3,1,"black")
    black.filling(2,2,"black")
    black.filling(1,3,"black")
    black.filling(0,4,"black")

    #for i in range(100):
        #black.filling(randint(0,14),randint(0,14),"black")

    print(black.condition_verticale("black"))
    print(black.condition_horizontal("black"))
    print(black.condition_diagonal("black"))   
    #print(black.L)



    Fenetre = App()

    area_draw = Canvas(Fenetre,width=WIDTH+2*OFFSET,height=WIDTH+2*OFFSET,bg="white", bd=0)
    area_draw.pack()
    #horizontal
    for i in range(LINES):
        area_draw.create_line(OFFSET,i*FACT+OFFSET,WIDTH+OFFSET,i*FACT+OFFSET, fill="black",width=2)
    for i in range(LINES):
        area_draw.create_line(i*FACT+OFFSET,OFFSET,i*FACT+OFFSET,WIDTH+OFFSET, fill="black",width=2)

    gomoku_test=Gomoku()
    for i in range(10):
        gomoku_test.bot()
        print("ha")

    Fenetre.mainloop()