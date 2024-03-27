from random import *



win_condition=5

DIMENSION=9
L_coordonates_vert=[]
L_coordonates_hori=[]
L_coordonates_diag=[]


win_rate=0

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
                    #print(L_coordonates_vert[-win_condition:])
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
                    #print(L_coordonates_hori[-win_condition:])
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
                    #print(L_coordonates_diag[-win_condition:])
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
                    #print(L_coordonates_diag[-win_condition:])
                    return("diag 2")
        L_coordonates_diag=[]
        return("no diag")



gomoku=Gomoku()

nbr_black=0
nbr_white=0

# L_temp --> liste temporaire des 15 parties aléatoires pour chaque coup
# L --> Liste de base à ne pas modifier durant L_temp
# L_all_coordonates --> coordonnées des pions placés dans les parties aléatoire


"""on a au depart black choisit par le joueur puis  avec white on fait jouer 15 parties aléatoires pour chaque coup et win rate"""

pawn="black"
counter=0
L=[[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]
x_first = 0
y_first = 0

L[x_first][y_first]="black"

L_winrate=[]


def coordonates_generation():
    L_all_coordonates=[]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if L[i][j]==None:
                tuple=(i,j)
                L_all_coordonates.append(tuple)

    shuffle(L_all_coordonates)
    return(L_all_coordonates)



def monte_carlo(i,j):
    global counter,pawn,win_rate,L_winrate

    winrate=0
    nbr_black=0
    nbr_white=0


    for x in range(15):
        gomoku_test=Gomoku()

        L_temp=gomoku_test.L

        L_temp[i][j]=pawn
        L_all_coordonates=coordonates_generation()


        for x in range(len(L_all_coordonates)):
            counter+=1
            if counter % 2==0:
               pawn="white"
            elif counter%2==1:
                 pawn="black"


            if pawn=="black":
               a=gomoku_test.condition_verticale("black")
               b=gomoku_test.condition_diagonal("black")
               c=gomoku_test.condition_horizontal("black")

               if a!="no vertical" or b!="no diag" or c!="no horizontal":
                  nbr_black+=1
                  break

            elif pawn=="white":
                 d=gomoku_test.condition_verticale("white")
                 e=gomoku_test.condition_diagonal("white")
                 f=gomoku_test.condition_horizontal("white")
                 if d!="no vertical" or e!="no diag" or f!="no horizontal" :
                    nbr_white+=1
                    winrate+=1
                    break

            L_temp[L_all_coordonates[x][0]][L_all_coordonates[x][1]]=pawn


    #print(L_temp)

    gomoku_test.L=[[None for _ in range(DIMENSION)] for _ in range(DIMENSION)]
    L_temp=gomoku_test.L


    winrate=int(winrate/15 *100)
    L_winrate.append(winrate)



for i in range(DIMENSION):
    for j in range(DIMENSION):
        monte_carlo(i,j)
print(L_winrate)