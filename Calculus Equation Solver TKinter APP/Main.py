import tkinter as tk
from Posicion_Falsa import Posicion_Falsa
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
top = tk.Tk()
#frame = tk.Frame(top)

def Falso():
    pass
menubar = tk.Menu(top)
codmenu = tk.Menu(menubar,tearoff=0)
codmenu.add_command(label="Posicion Falsa",command=Falso)
codmenu.add_separator()

incio = tk.Text(top)
incio.insert(tk.INSERT,"HOLa")


top.config(menu=menubar)
top.mainloop()