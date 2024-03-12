from tkinter import *

Fenetre = Tk()

area_draw = Canvas(Fenetre,width=225,height=225,bg="white", bd=0)
area_draw.pack()
#horizontal
for i in range(16):

    area_draw.create_line(0,0+15,225,0+15, fill="black",width=2)

area_draw.create_line(10,225,10,0, fill="black",width=2)
Fenetre.mainloop()

class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.bind("-", lambda e: self.dezoom())
        self.bind("<BackSpace>", lambda e: self.retour_vue_precedente())
        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))
        self.bind('<ButtonRelease-1>', lambda e: self.click_relache(e.x, e.y))

        # gestion des coordonnées pour l'image
        # au depart on trace l'image de cote [-2, 2]
        self.xmin, self.ymin = -2, -2
        self.xmax, self.ymax = 2, 2

        # vous pouvez ajouter des attributes pour gérer le zoom dans un rectangle

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img

    def dezoom(self):
        print("-") # a modifier

    def click(self, x, y):
        print("click", x, y) # a modifier

    def click_relache(self, x, y):
        print("relache", x, y) # a modifier

    def retour_vue_precedente(self):
        print("retour") # a modifier