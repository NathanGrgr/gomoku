from tkinter import *



class Gomoku:
    def __init__(self):
        self.L=[[None for i in range(15)] for i in range(15)]


    def fullfill(self,i,j,pawn):
        self.L[i][j]=pawn
        return (self.L[i][j])


    def condition_verticale(self,pawn):
        counter=0
        print(self.L)
        for i in self.L:
            for x in range(len(self.L)):
                if i[x]==pawn:
                    counter+=1
                    for j in range(13):
                        if self.L[self.L.index(i)][j+1]!=None:
                            counter+=1
                            if counter==5:
                                return("verticale")
        return(counter)


    def condition_horizontal(self,pawn):
        counter=0
        print(self.L)
        for i in self.L:
            for x in range(len(self.L)):
                if i[x]==pawn:
                    counter+=1
                if counter==5:
                    return("horizontal")


    def condition_diagonal(self,pawn):
        counter=0
        print(self.L)
        for i in range(len(self.L)):
            for j in range(len(self.L)):
                if j>len(self.L)-5 and counter==0:
                    return("non")
                elif self.L[i][j]==pawn:
                    counter+=1
        if counter==5:
            return("diag")

        #check diagonal dans l'autre sens
        else:
            counter=0
            for i in range((len(self.L)-1), -1, -1):
                for j in range(len(self.L)):
                    if j<5 and counter==0:
                        return("debut de diagonal mais pas la taille")
                    if self.L[i][j]==pawn:
                        counter+=1
            if counter==5:
                return("diag inverse")


#3,0 2,1 1,0
#changer diagonale + checker sens horizontal et verticale
if __name__=="__main__":
    black=Gomoku()
    black.fullfill(0,0,"black")
    black.fullfill(1,1,"black")
    black.fullfill(2,2,"black")
    black.fullfill(3,3,"black")
    black.fullfill(4,4,"black")
    print(black.condition_diagonal("black"))