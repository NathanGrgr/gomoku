from tkinter import *
import math

FACT=30
LINES=16
WIDTH=FACT*(LINES-1)
OFFSET=10
RADIUS=10

class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img

    def click(self, x, y):
        xr=OFFSET+math.floor((x+FACT/2-OFFSET)/FACT)*FACT
        yr=OFFSET+math.floor((y+FACT/2-OFFSET)/FACT)*FACT
        print("click", x, y,"->",xr,yr)
        area_draw.create_oval(xr-RADIUS,yr-RADIUS,xr+RADIUS,yr+RADIUS,fill="black", outline="green")

Fenetre = App()

area_draw = Canvas(Fenetre,width=WIDTH+2*OFFSET,height=WIDTH+2*OFFSET,bg="white", bd=0)
area_draw.pack()
#horizontal
for i in range(LINES):
    area_draw.create_line(OFFSET,i*FACT+OFFSET,WIDTH+OFFSET,i*FACT+OFFSET, fill="black",width=2)
for i in range(LINES):
    area_draw.create_line(i*FACT+OFFSET,OFFSET,i*FACT+OFFSET,WIDTH+OFFSET, fill="black",width=2)

Fenetre.mainloop()
