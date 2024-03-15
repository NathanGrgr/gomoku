from tkinter import *
import math
from random import randint
from PIL import ImageTk


L_history_white=[]
L_history_black=[]
L_history_oval_black=[]
L_history_oval_white=[]
DIMENSION=15
FACT=50 #écart entre chaque case
LINES=DIMENSION
WIDTH=FACT*(LINES-1)
OFFSET=20 #remplissage avant
RADIUS=20 #écart après
win_condition=5
nbr_white=0
nbr_black=0


#taille case --> 30


class Gomoku:
    def __init__(self):
        self.L=[[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]


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

#00 11 22 diag 1
#4,0 3,1 2,2 1,3 0,4 diag 2


gomoku=Gomoku()


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
        self.bind("<BackSpace>", lambda e: self.retour())

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img


    def click(self, x, y):
        global nbr_white
        global nbr_black

        nbr_None=counting(L)

        xr=OFFSET+math.floor((x+FACT/2-OFFSET)/FACT)*FACT
        yr=OFFSET+math.floor((y+FACT/2-OFFSET)/FACT)*FACT

        x=(xr*LINES)//(WIDTH+2*OFFSET)
        y=(yr*LINES)//(WIDTH+2*OFFSET)
        tuple=(x,y)
        L_history_black.append(tuple)

        if L[y][x]==None:
           L[y][x]="black"
           self.oval_black=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="black")
           L_history_oval_black.append(self.oval_black)
           nbr_black+=1

        if len(L_history_black)>1:
            if  L_history_black[-2]!=L_history_black[-1]:
                x_alea=randint(0,WIDTH)
                y_alea=randint(0,WIDTH)

                xr=OFFSET+math.floor((x_alea+FACT/2-OFFSET)/FACT)*FACT
                yr=OFFSET+math.floor((y_alea+FACT/2-OFFSET)/FACT)*FACT

                x=(xr*LINES)//(WIDTH+2*OFFSET)
                y=(yr*LINES)//(WIDTH+2*OFFSET)

                if L[y][x]==None and nbr_white==nbr_black-1:
                    tuple=(x,y)
                    L_history_white.append(tuple)
                    L[y][x]="white"
                    self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="white")
                    L_history_oval_white.append(self.oval_white)
                    nbr_white+=1

                else:
                    if nbr_None<2:
                        pass
                    else:
                        while L[y][x]!=None:
                            x_alea=randint(0,WIDTH)
                            y_alea=randint(0,WIDTH)
                            xr=OFFSET+math.floor((x_alea+FACT/2-OFFSET)/FACT)*FACT
                            yr=OFFSET+math.floor((y_alea+FACT/2-OFFSET)/FACT)*FACT
                            x=(xr*LINES)//(WIDTH+2*OFFSET)
                            y=(yr*LINES)//(WIDTH+2*OFFSET)
                            if nbr_white == nbr_black-1 and L[y][x]==None:
                                L[y][x]="white"
                                self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="white")
                                L_history_oval_white.append(self.oval_white)
                                nbr_white+=1
                                tuple=(x,y)
                                L_history_white.append(tuple)
                                break

        else:
             x_alea=randint(0,WIDTH)
             y_alea=randint(0,WIDTH)

             xr=OFFSET+math.floor((x_alea+FACT/2-OFFSET)/FACT)*FACT
             yr=OFFSET+math.floor((y_alea+FACT/2-OFFSET)/FACT)*FACT

             x=(xr*LINES)//(WIDTH+2*OFFSET)
             y=(yr*LINES)//(WIDTH+2*OFFSET)

             tuple=(x,y)
             L_history_white.append(tuple)
             if L[y][x]==None:
                L[y][x]="white"
                self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="white")
                L_history_oval_white.append(self.oval_white)
                nbr_white+=1

        #print(L)
        #print("black :",nbr_black)
        #print("white :",nbr_white)
        #print(L_history_black)
        #print(L_history_white)







    def retour(self,compt=1):
        global nbr_black
        global nbr_white

        L_history_black_sort,L_history_white_sort=history(L)
        area_draw.delete(L_history_oval_black[-compt])
        L_history_oval_black.pop(-1)

        area_draw.delete(L_history_oval_white[-compt])
        L_history_oval_white.pop(-1)
        nbr_black-=1
        nbr_white-=1
        compt+=1


        Tuple_black=L_history_black_sort[-1]
        x=Tuple_black[0]
        y=Tuple_black[1]
        L[y][x]=None

        Tuple_white=L_history_white_sort[-1]
        x=Tuple_white[0]
        y=Tuple_white[1]
        L[y][x]=None


        L_history_black_sort.pop(-1)
        L_history_white_sort.pop(-1)

        if len(L_history_black_sort)==0:
            L_history_black=[]
            L_history_white=[]



def history(L):
    L_history_black_update=[]
    L_history_white_update=[]
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]=="black":
               tuple=(j,i)
               L_history_black_update.append(tuple)
            elif L[i][j]=="white":
               tuple=(j,i)
               L_history_white_update.append(tuple)
    return(L_history_black_update,L_history_white_update)



def counting(L):
    count=0
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]==None:
                count+=1
    return(count)


Fenetre = App()

area_draw = Canvas(Fenetre,width=WIDTH+2*OFFSET,height=WIDTH+2*OFFSET,bg="white", bd=0)
area_draw.pack()


for i in range(LINES):
    area_draw.create_line(OFFSET,i*FACT+OFFSET,WIDTH+OFFSET,i*FACT+OFFSET, fill="black",width=2)
for i in range(LINES):
    area_draw.create_line(i*FACT+OFFSET,OFFSET,i*FACT+OFFSET,WIDTH+OFFSET, fill="black",width=2)


Fenetre.mainloop()





"""
def inverse_list(L):
    L_new=[]
    for i in range(len(L),-1,-1):
       L_new.append(L[i])
    print(L)
    print(L_new)
"""