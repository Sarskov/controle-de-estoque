from tkinter import *
import sqlite3

#conn = sqlite3.connect("C:\TkinterVenda\Database\store.db")
#c = conn.cursor()

#result = c.execute("SELECT MAX(id) from inventory")
#for r in result:
 #   id = r[0]

class Tkinter:
    def __init__(self):

        #self.master = master
        #self.heading = Label(master, Text="Cadastro De Produtos",font=('arial 40 bold'), fg='steelblue')
        #self.heading.place(x=400,y=0)

        self.name_1= Label( Text="nome",font=('arial 18 bold'))
        self.name_1.place(x=0,y=70)

Root = Tk()


b = Tkinter(Root)

Root.geometry("1366x768+0+0")
Root.title("FORMULARIO DE CADASTRO")
Root.mainloop()

