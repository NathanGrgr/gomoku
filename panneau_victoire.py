from tkinter import Tk, Button, Label

class MyWindow(Tk):

    def __init__(self):
        super().__init__()
        label = Label(self, text="Félicitation vous avez gagner", fg="white", bg="#4A919E")
        label.pack(side="top", fill='x')
        button = Button(self, text="1 Player", fg="white", bg="#FF00FF", command=self.player_vs_bot)
        button.place(x=200,y=100)
        button1 = Button(self, text=" 2 Player ", command=self.playeur_vs_player)
        button.ack()
        button = Button(self, text=" Quitter ", fg="black", bg="blue")
        button.place(x=400,y=250)
        first_label = Label(self, text=" ", fg="white", bg="#4A919E")
        first_label.pack(side="bottom", fill='x')
        self.geometry("450x300")
        self.title("GOMOKU")

#place(x=200,y=100)
    def player_vs_player(self):
        super().__init__()
        label.title("Nouvelle partie Joueur contre Joueur")
        print("nv pt ply vs ply")
        self.geometry("450x300")
        self.title("Nouvelle partie")
    def player_vs_bot(self):
        supe().__init__()
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

# On crée notre fenêtre et on l'affiche
window = MyWindow()
window.mainloop()

"""
first_label = Label(self, text="Label (10, 10)", fg="white", bg="#FF00FF")
        first_label.place(x=10, y=10)

first_label = Label(self, text="Label (10, 10)", fg="white", bg="#FF00FF")
        first_label.place(x=10, y=10)
button = Button(self, text="Push me !", command=self.do_something)
        button.pack()
command=self.do_something
        second_label = Label(self, text="Label (50, 50)", fg="white", bg="green")
        second_label.place(x=50, y=50)

        button = Button(self, text="Button (90, 90)", fg="black", bg="blue")
        button.place(x=90, y=90)
"""
https://docs.python.org/fr/3/library/tkinter.html
https://www.palettedecouleur.net/
https://koor.fr/Python/Tutoriel_Tkinter/tkinter_premiere_fenetre.wp

"""
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
"""