from tkinter import *
import math
from random import randint

L_historique_b=[]
L_historique_n=[]
FACT=30 #écart entre chaque case
LINES=15
WIDTH=FACT*(LINES-1)
OFFSET=10
RADIUS=10
win_condition=5

#taille grille --> 30




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


gomoku=Gomoku()

#for i in range(100):
    #gomoku.filling(randint(0,14),randint(0,14),"black")
"""
print(gomoku.condition_verticale("black"))
print(gomoku.condition_horizontal("black"))
print(gomoku.condition_diagonal("black"))
print(gomoku.L)
"""
L=gomoku.L
COUNTER=0




class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img

    def click(self, x, y):
        xr=OFFSET+math.floor((x+FACT/2-OFFSET)/FACT)*FACT
        yr=OFFSET+math.floor((y+FACT/2-OFFSET)/FACT)*FACT


        x=(xr*LINES)//(WIDTH+2*OFFSET)
        y=(yr*LINES)//(WIDTH+2*OFFSET)
        if L[y][x]==None:
           L[y][x]="black"
           area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="black")
           print(L)
        else:
             pass

        Tuple=(x,y)
        L_historique_n.append(Tuple)

        if len(L_historique_n)>1:
            if  L_historique_n[0]==L_historique_n[1]:
                x_alea=randint(0,WIDTH)
                y_alea=randint(0,WIDTH)
                xr=OFFSET+math.floor((x_alea+FACT/2-OFFSET)/FACT)*FACT
                yr=OFFSET+math.floor((y_alea+FACT/2-OFFSET)/FACT)*FACT

                x=(xr*LINES)//(WIDTH+2*OFFSET)
                y=(yr*LINES)//(WIDTH+2*OFFSET)
                L[y][x]="white"
                area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="white")
        else:
            pass

        Tuple=(x,y)
        L_historique_b.append(Tuple)
        print(L_historique_n)
        print(L_historique_b)

    def bot(self):
        pass



Fenetre = App()

area_draw = Canvas(Fenetre,width=WIDTH+2*OFFSET,height=WIDTH+2*OFFSET,bg="white", bd=0)
area_draw.pack()

#horizontal
for i in range(LINES):
    area_draw.create_line(OFFSET,i*FACT+OFFSET,WIDTH+OFFSET,i*FACT+OFFSET, fill="black",width=2)
for i in range(LINES):
    area_draw.create_line(i*FACT+OFFSET,OFFSET,i*FACT+OFFSET,WIDTH+OFFSET, fill="black",width=2)

COUNTER=COUNTER%2



Fenetre.mainloop()
