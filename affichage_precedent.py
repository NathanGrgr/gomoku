from tkinter import Tk, Button, Label

class MyWindow(Tk):

        def __init__(self):
            super().__init__()
            label = Label(self, text="Bienvenue", fg="white", bg="#4A919E")
            label.pack(side="top", fill='x')
            button = Button(self, text="1 Player", fg="white", bg="#A7001E", command=self.p_vs_bot)
            button.place(x=100,y=110)
            button = Button(self, text=" 2 Player ", fg="white", bg="#A7001E", command=self.p_vs_p)
            button.place(x=300,y=110)
            button = Button(self, text=" Bot vs Bot ", fg="white", bg="#A7001E", command=self.bot_vs_bot)
            button.place(x=200,y=110)
            button = Button(self, text=" Quitter ", fg="red", bg="blue", command=self.destroy)
            button.place(x=390,y=250)
            first_label = Label(self, text=" ", fg="white", bg="#4A919E")
            first_label.pack(side="bottom", fill='x')
            self.geometry("450x300")
            self.title("GOMOKU")

#place(x=200,y=100)

        def p_vs_p(self):
            super().__init__()
            label.title("Nouvelle partie Joueur contre Joueur")
            print("nv pt ply vs ply")
            self.geometry("450x300")
            self.title("Nouvelle partie")

        def p_vs_bot(self):
            super().__init__()
            label.title("Nouvelle partie Joueur contre Bot")
            print("nv p bot")
            self.geometry("450x300")
            self.title("Nouvelle partie")




        def do_something(self):
            super().__init__()
            label = Label(self, text="Félicitation vous avez gagner")
            label.pack()
            button = Button(self, text="Continue !", command=self.do_something)
            button.pack()
            self.geometry("450x300")
            self.title("Nouvelle partie")

        def bot_vs_bot(self):
            super().__init__()
            label.title(" ")
            print(" ")
            self.geometry("450x300")
            self.title("Nouvelle partie")

# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()


