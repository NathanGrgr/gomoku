from tkinter import Tk, Button, Label


def victory():            
            enable_command=False
            class MyWindow(Tk):
                def __init__(self):
                    super().__init__()
                    label = Label(self, text="Félicitation vous avez gagné", fg="white", bg="#4A919E")
                    label.pack(side="top", fill='x')
                    button = Button(self, text="1 Player", fg="white", bg="#FF00FF", command=self.player_vs_bot)
                    button.place(x=200,y=100)
                    button1 = Button(self, text=" 2 Player ", command=self.player_vs_player)
                    button.pack()
                    button = Button(self, text=" Quitter ", fg="black", bg="blue")
                    button.place(x=400,y=250)
                    first_label = Label(self, text=" ", fg="white", bg="#4A919E")
                    first_label.pack(side="bottom", fill='x')
                    self.geometry("450x300+700+300")
                    self.title("GOMOKU")

                #place(x=200,y=100)
                def player_vs_player(self):
                    super().__init__()
                    Label.title("Nouvelle partie Joueur contre Joueur")
                    print("nv pt ply vs ply")
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")
                def player_vs_bot(self):
                    super().__init__()
                    Label.title("Nouvelle partie Joueur contre Bot")
                    print("nv p bot")
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")
                def do_something(self):
                    super().__init__()
                    label = Label(self, text="Félicitation vous avez gagné")
                    label.pack()
                    button = Button(self, text="Continue !", command=self.do_something)
                    button.pack()
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")

            # On crée notre fenêtre et on l'affiche
            window = MyWindow()
            window.mainloop() 





"""match nul"""
def draw():  
            class MyWindow(Tk):

                def __init__(self):
                    super().__init__()
                    label = Label(self, text="Match Nul", fg="white", bg="#4A919E")
                    label.pack(side="top", fill='x')
                    button = Button(self, text="1 Player", fg="white", bg="#FF00FF", command=self.player_vs_bot)
                    button.place(x=200,y=100)
                    button1 = Button(self, text=" 2 Player ", command=self.player_vs_player)
                    button.pack()
                    button = Button(self, text=" Quitter ", fg="black", bg="blue")
                    button.place(x=400,y=250)
                    first_label = Label(self, text=" ", fg="white", bg="#4A919E")
                    first_label.pack(side="bottom", fill='x')
                    self.geometry("450x300+700+300")
                    self.title("GOMOKU")

                #place(x=200,y=100)
                def player_vs_player(self):
                    super().__init__()
                    Label.title("Nouvelle partie Joueur contre Joueur")
                    print("nv pt ply vs ply")
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")
                def player_vs_bot(self):
                    super().__init__()
                    Label.title("Nouvelle partie Joueur contre Bot")
                    print("nv p bot")
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")
                def do_something(self):
                    super().__init__()
                    label = Label(self, text="Félicitation vous avez gagné")
                    label.pack()
                    button = Button(self, text="Continue !", command=self.do_something)
                    button.pack()
                    self.geometry("450x300+700+300")
                    self.title("Nouvelle partie")

            # On crée notre fenêtre et on l'affiche
            window = MyWindow()
            window.mainloop() 


