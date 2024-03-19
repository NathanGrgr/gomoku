from tkinter import Tk, Button, Label

class Window(Tk):

        def __init__(self):
            super().__init__()
            label = Label(self, text="Défaite", fg="white", bg="#A7001E")
            label.pack(side="top", fill='x')
            button = Button(self, text="Menu principal", fg="white", bg="#A7001E", command=self.menu)
            button.place(x=100,y=110)
            button = Button(self, text=" Quitter ", fg="red", bg="blue", command=self.destroy)
            button.place(x=290,y=110)
            first_label = Label(self, text=" ", fg="white", bg="#A7001E")
            first_label.pack(side="bottom", fill='x')
            self.geometry("450x300")
            self.title("GOMOKU")

#place(x=200,y=100)
        def menu(self):
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

window = Window()
window.mainloop()