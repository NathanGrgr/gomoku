from tkinter import *
from tkinter import Tk, Button, Label
from random import randint
from random import *
from PIL import ImageTk
from gomoku_affichage import *
import time
import math


"""
bug Bot vs Bot avec :

line 451, in <module>
botvsbot()
line 447, in botvsbot
Fenetre.bot("black")
line 322, in bot
self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
"""

# + bug coordonnées validant condition + faire algo alphabeta (minmax)
# + bug retour player vs player
# faire programme pour compter coordonnées et des qu'on est a 5 on affiche


class MyWindow(Tk):

        def __init__(self):
            super().__init__()
            label = Label(self, text="Bienvenue", fg="white", bg="#4A919E")
            label.pack(side="top", fill='x')
            button = Button(self, text="Player vs Player", fg="white", bg="#A7001E", command=self.p_vs_p)
            button.place(x=100,y=110)
            button = Button(self, text="Player vs Bot", fg="white", bg="#A7001E", command=self.p_vs_bot)
            button.place(x=300,y=110)
            button = Button(self, text=" Bot vs Bot ", fg="white", bg="#A7001E", command=self.bot_vs_bot)
            button.place(x=200,y=110)
            button = Button(self, text=" Quitter ", fg="red", bg="blue", command=self.quit)
            button.place(x=390,y=250)

            first_label = Label(self, text=" ", fg="white", bg="#4A919E")
            first_label.pack(side="bottom", fill='x')
            self.geometry("450x300")
            self.title("GOMOKU")


        def do_something(self):
            super().__init__()
            label = Label(self, text="Félicitations, vous avez gagné")
            label.pack()
            button = Button(self, text="Continue !", command=self.do_something)
            button.pack()
            self.geometry("450x300")
            self.title("Nouvelle partie")

        def p_vs_p(self):
            global input
            input=1
            self.destroy()

        def p_vs_bot(self):
            global input
            input=2
            self.destroy()

        def bot_vs_bot(self):
            global input
            input=3
            self.destroy()

        def quit(self):
            global input
            input=4
            self.destroy()




# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()


#1 player vs player
#2 player vs bot
#3 bot vs bot
#faire calcul pour dimension 1er fenetre gomoku_affichage + mode PvAI + AIvAI


L_history_white=[]
L_history_black=[]
L_history_oval_black=[]
L_history_oval_white=[]

L_coordonates_vert=[]
L_coordonates_hori=[]
L_coordonates_diag=[]

DIMENSION=15
FACT=50 #écart entre chaque case
LINES=DIMENSION
WIDTH=FACT*(LINES-1)
OFFSET=20 #remplissage avant
RADIUS=20 #écart après
win_condition=5
nbr_white=0
nbr_black=0
enable_command=True
threshold=int((DIMENSION*DIMENSION)/2)

#taille case --> 30



class Gomoku:
    def __init__(self):
        self.L=[[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]


    def filling(self,i,j,pawn):
        self.L[i][j]=pawn
        return (self.L[i][j])


    def condition_verticale(self,pawn):
        global L_coordonates_vert

        for i in range(len(self.L)):
            for j in range(len(self.L)):
                counter=0
                for k in range(win_condition):
                    if i+k<len(self.L)and self.L[i+k][j]==pawn:
                        tuple=(i+k,j)
                        L_coordonates_vert.append(tuple)
                        counter+=1
                if counter==win_condition:
                    print(L_coordonates_vert[-win_condition:])
                    return("vertical")
        L_coordonates_vert=[]
        return("no vertical")


    def condition_horizontal(self,pawn):
        global L_coordonates_hori

        for i in range(len(self.L)):
            for j in range(len(self.L)):
                counter=0
                for k in range(win_condition):
                    if j+k<len(self.L)and self.L[i][j+k]==pawn:
                        tuple=(i,j+k)
                        L_coordonates_hori.append(tuple)
                        counter+=1
                if counter==win_condition:
                    print(L_coordonates_hori[-win_condition:])
                    return("horizontal")
        L_coordonates_hori=[]
        return("no horizontal")


    def condition_diagonal(self,pawn):
        global L_coordonates_diag

        for i in range(len(self.L)):
            for j in range(len(self.L)):
                counter=0
                for k in range(win_condition):
                    if i+k<len(self.L)and j+k<len(self.L)and self.L[i+k][j+k]==pawn:
                        tuple=(i+k,j+k)
                        L_coordonates_diag.append(tuple)
                        counter+=1
                if counter==win_condition:
                    print(L_coordonates_diag[-win_condition:])
                    return("diag 1")
        L_coordonates_diag=[]
        for i in range(len(self.L)):
            for j in range(len(self.L)):
                counter=0
                for k in range(win_condition):
                    if i+k<len(self.L)and j-k>=0 and self.L[i+k][j-k]==pawn:
                        tuple=(i+k,j-k)
                        L_coordonates_diag.append(tuple)
                        counter+=1
                if counter==win_condition:
                    print(L_coordonates_diag[-win_condition:])
                    return("diag 2")
        L_coordonates_diag=[]
        return("no diag")

#L_coordonates --> coordonnées des pions alignées after

#i nombre de ligne
#j nombre d'éléments à l'intérieur de la ligne

#00 11 22 diag 1
#4,0 3,1 2,2 1,3 0,4 diag 2


def history(L):
    """Historique des coordonnées des points placés"""
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


gomoku=Gomoku()
L=gomoku.L
L_history_black_up,L_history_white_up=(history(L))
pawn="black"
COUNTER=0


class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        if input!=3:
            self.bind('<Button-1>', lambda e: self.click(e.x, e.y,pawn))
        self.bind("<BackSpace>", lambda e: self.retour())

        button= Button(self,text="reset",fg="white",bg="blue",command=self.reset)
        self.geometry("800x800+520+120")


    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img


    def click(self, x, y,pawn="black"):
        global nbr_white,nbr_black

        if input==1:
            global COUNTER

            COUNTER=COUNTER%2
            if COUNTER==0:
                pawn="black"
            if COUNTER==1:
                pawn="white"

        self.tk_vict()
        xr=OFFSET+math.floor((x+FACT/2-OFFSET)/FACT)*FACT
        yr=OFFSET+math.floor((y+FACT/2-OFFSET)/FACT)*FACT

        x=(xr*LINES)//(WIDTH+2*OFFSET)
        y=(yr*LINES)//(WIDTH+2*OFFSET)
        tuple=(x,y)
        L_history_black.append(tuple)

        if y>14 or x>14:
            pass

        elif L[y][x]==None and enable_command==True:
           L[y][x]=pawn
           if pawn=="black":
              self.oval_black=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
              L_history_oval_black.append(self.oval_black)
              nbr_black+=1
           else:
                self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                L_history_oval_white.append(self.oval_white)
                nbr_white+=1
           COUNTER+=1

        if input==2:
            self.bot("white")



    def bot(self,pawn):
        global nbr_white,nbr_black

        nbr_None=counting(L)
        if len(L_history_black)>1:
            if  L_history_black[-2]!=L_history_black[-1]:
                """Eviter les répétitions"""
                x_alea=randint(0,WIDTH)
                y_alea=randint(0,WIDTH)

                xr=OFFSET+math.floor((x_alea+FACT/2-OFFSET)/FACT)*FACT
                yr=OFFSET+math.floor((y_alea+FACT/2-OFFSET)/FACT)*FACT

                x=(xr*LINES)//(WIDTH+2*OFFSET)
                y=(yr*LINES)//(WIDTH+2*OFFSET)

                if L[y][x]==None and nbr_white==nbr_black-1:
                    tuple=(x,y)
                    L_history_white.append(tuple)
                    L[y][x]=pawn

                    if pawn=="white":
                        self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                        L_history_oval_white.append(self.oval_white)
                        nbr_white+=1
                    else:
                        self.oval_black=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                        L_history_oval_black.append(self.oval_black)
                        nbr_black+=1
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
                                L[y][x]=pawn
                                tuple=(x,y)

                                if pawn=="white":
                                    self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                                    L_history_oval_white.append(self.oval_white)
                                    nbr_white+=1

                                    L_history_white.append(tuple)
                                else:
                                    self.oval_black=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                                    L_history_oval_black.append(self.oval_black)
                                    nbr_black+=1
                                    L_history_black.append(tuple)
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
                L[y][x]=pawn

                if pawn=="white":
                    self.oval_white=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                    L_history_oval_white.append(self.oval_white)
                    nbr_white+=1
                else:
                    self.oval_black=area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill=pawn)
                    L_history_oval_black.append(self.oval_black)
                    nbr_black+=1

        #print(L)
        #print("black :",nbr_black)
        #print("white :",nbr_white)
        #print("None :",nbr_None)
        #print(L_history_black)
        #print(L_history_white)

        self.tk_vict()



    def tk_vict(self):
        """repérage de fin de partie"""
        global enable_command

        a=gomoku.condition_verticale("black")
        b=gomoku.condition_diagonal("black")
        c=gomoku.condition_horizontal("black")

        d=gomoku.condition_verticale("white")
        e=gomoku.condition_diagonal("white")
        f=gomoku.condition_horizontal("white")

        if a=="vertical" or b=="diag 1" or b=="diag 2" or c=="horizontal" or d=="vertical" or e=="diag 1" or e=="diag 2" or f=="horizontal" and enable_command==True :
            enable_command=False

            victory()

        elif nbr_black>threshold and enable_command==True:
            draw()


    def retour(self,compt=1):
        global nbr_black
        global nbr_white
        global enable_command

        enable_command=True

        L_history_black_sort,L_history_white_sort=history(L)
        area_draw.delete(L_history_oval_black[-compt])
        L_history_oval_black.pop(-1)
        nbr_black-=1

        area_draw.delete(L_history_oval_white[-compt])
        L_history_oval_white.pop(-1)
        nbr_white-=1

        compt+=1


        Tuple_white=L_history_white_sort[-1]
        x=Tuple_white[0]
        y=Tuple_white[1]
        L[y][x]=None


        Tuple_black=L_history_black_sort[-1]
        x=Tuple_black[0]
        y=Tuple_black[1]
        L[y][x]=None


        L_history_black_sort.pop(-1)
        L_history_white_sort.pop(-1)

        return(enable_command)



    def reset(self):
        L_history_black_sort,L_history_white_sort=history(L)
        for i in range(len(L_history_black_sort)):
            Tuple_white=L_history_white_sort[-1]
            x=Tuple_white[0]
            y=Tuple_white[1]
            L[y][x]=None


            Tuple_black=L_history_black_sort[-1]
            x=Tuple_black[0]
            y=Tuple_black[1]
            L[y][x]=None


            L_history_black_sort.pop(-1)
            L_history_white_sort.pop(-1)




def counting(L):
    count=0
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]==None:
                count+=1
    return(count)



class Monte_Carlo:
      def __init__(self,valeur=None):
          self.valeur=valeur
          self.fils=[]


def monte_carlo():
    L_all_coordonates=[]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            tuple=(i,j)
            L_all_coordonates.append(tuple)

    L_fils=L_all_coordonates

    shuffle(L_all_coordonates)

    L_temp=[[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    L_temp[0][0]="black"
    L_fils.pop(0)


    for i in range((DIMENSION*DIMENSION)-2):
        pass




if __name__=="__main__":
    Fenetre = App()
    area_draw = Canvas(Fenetre,width=WIDTH+2*OFFSET,height=WIDTH+2*OFFSET,bg="grey", bd=0)
    area_draw.pack()
    button = Button(Fenetre, text=" Reset ", command=Fenetre.reset)
    button.place(x=0,y=250)
    def grid(area_draw):

        for i in range(LINES):
            area_draw.create_line(OFFSET,i*FACT+OFFSET,WIDTH+OFFSET,i*FACT+OFFSET, fill="black",width=2)
        for i in range(LINES):
            area_draw.create_line(i*FACT+OFFSET,OFFSET,i*FACT+OFFSET,WIDTH+OFFSET, fill="black",width=2)
    grid(area_draw)
    def reset(self):
        global input
        input=5
        self.destroy()
    def botvsbot():
        a=gomoku.condition_verticale("black")
        b=gomoku.condition_diagonal("black")
        c=gomoku.condition_horizontal("black")

        d=gomoku.condition_verticale("white")
        e=gomoku.condition_diagonal("white")
        f=gomoku.condition_horizontal("white")

        while a=="no vertical" or b=="no diag" or c=="no horizontal" or d=="no vertical" or e=="no diag" or f=="no horizontal" :
              Fenetre.bot("black")
              Fenetre.bot("white")



    print(monte_carlo())

    if input==3:
        botvsbot()
    if input==5:
        area_draw.delete("all")
        grid(area_draw)
        L_history_black=[]
        L_history_white=[]

    if input!=4:
        Fenetre.mainloop()
