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

pawn="white"
counter=0

x_first = 0
y_first = 0

gomoku.L[x_first][y_first]="black"
L= [[gomoku.L[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]
#print(L)
L_winrate=[]
L_winrate_coordonates=[]

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
    global counter,pawn,win_rate,L_winrate,L_winrate_coordonates,gomoku

    winrate=0
    nbr_black=0
    nbr_white=0
    

    for x in range(15):
        L_all_coordonates=coordonates_generation()
        L_temp= [[L[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]
        #print(L_temp)
        L_temp[i][j]=pawn

        
        coord_to_remove = (i, j)
        if coord_to_remove in L_all_coordonates:
            index = L_all_coordonates.index(coord_to_remove)
            L_all_coordonates.pop(index)
        
        #print(L_temp,"n")


        for k in range(len(L_all_coordonates)):


            L_temp[L_all_coordonates[k][0]][L_all_coordonates[k][1]]=pawn

            gomoku.L=L_temp
            counter+=1
            if counter % 2==0:
               pawn="white"
            elif counter%2==1:
                 pawn="black"


            if pawn=="black":
               a=gomoku.condition_verticale("black")
               b=gomoku.condition_diagonal("black")
               c=gomoku.condition_horizontal("black")

               if a!="no vertical" or b!="no diag" or c!="no horizontal":
                  nbr_black+=1
                  break

            elif pawn=="white":
                 d=gomoku.condition_verticale("white")
                 e=gomoku.condition_diagonal("white")
                 f=gomoku.condition_horizontal("white")
                 if d!="no vertical" or e!="no diag" or f!="no horizontal" :
                    nbr_white+=1
                    winrate+=1
                    break

            
            #print(L_temp,"temp",x)

    #print(L_temp)
    gomoku.L=L
    
    L_temp=L
    #print(L,"L")
    winrate=int(winrate/15 *100)

    tuple=((i,j),(winrate))

    L_winrate_coordonates.append(tuple)

    L_winrate.append(winrate)




def listage_coordonates(liste_None=[]):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]==None:
                liste_None.append((i,j))
    return(liste_None)



liste_None=listage_coordonates()

for i in liste_None:
    monte_carlo(i[0],i[1])

#print(L_winrate)

#print(L_winrate_coordonates)
#print(gomoku.L)


for i in L_winrate_coordonates:
    if i[1]==max(L_winrate): #and i[0] in liste_None
        print(i)
        break

