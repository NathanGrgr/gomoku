from tkinter import Tk, Button, Label

enable_command=True

def victory():
    global enable_command
    if enable_command == True:
            enable_command=False

            class Window(Tk):

                def __init__(self):
                    super().__init__()
                    label = Label(self, text="Victoire", fg="white", bg="#8FB43A")
                    label.pack(side="top", fill='x')
                    button = Button(self, text=" Quitter ", fg="red", bg="blue", command=self.destroy)
                    button.place(x=290,y=110)
                    first_label = Label(self, text=" ", fg="white", bg="#8FB43A")
                    first_label.pack(side="bottom", fill='x')
                    self.geometry("450x300")
                    self.title("GOMOKU")

            window = Window()
            window.mainloop()




"""match nul"""
def draw():
    global enable_command
    if enable_command == True:
            enable_command=False

            class Window(Tk):

                def __init__(self):
                    super().__init__()
                    label = Label(self, text="Défaite", fg="white", bg="#A7001E")
                    label.pack(side="top", fill='x')
                    button = Button(self, text="Menu principal", fg="white", bg="#A7001E", command=self.menu)
                    button.place(x=100,y=110)
                    button = Button(self, text="Quitter", fg="red", bg="blue", command=self.destroy)
                    button.place(x=290,y=110)
                    first_label = Label(self, text=" ", fg="white", bg="#A7001E")
                    first_label.pack(side="bottom", fill='x')
                    self.geometry("450x300")
                    self.title("GOMOKU")

            window = Window()
            window.mainloop()
