from tkinter import *
from SolEcuaciones import *
from Interpolacion import *
from Funcion import *
from Differ import *
from sympy import *

class MenuP:
    def __init__(self):
        self.window = Tk()
        self.window.title("CN")
        self.window.geometry("450x450")
        self.window.iconbitmap('Suma.ico')
        self.window.resizable(width=False, height=False)
        lbl = Label(self.window, text=" : - : - : - : - : - : - : - : - : - : - : - : ")
        lbl.config(font=("Arial", 25))
        lbl.grid(row=0, column=0, columnspan=3)
        lbl = Label(self.window, text="")
        lbl.grid(column=2, row=1)
        lbl = Label(self.window, text=" > ")
        lbl.config(font=("", 20))
        lbl.grid(column=0, row=2)
        lbl = Label(self.window, text=" > ")
        lbl.config(font=("", 20))
        lbl.grid(column=0, row=3)
        lbl = Label(self.window, text=" > ")
        lbl.config(font=("", 20))
        lbl.grid(row=4, column=0)
        lbl = Label(self.window, text=" > ")
        lbl.config(font=("", 20))
        lbl.grid(row=5, column=0)
        lbl = Label(self.window, text="Please be sure to read (Help?) info before calculating,\n some functions change based on the topic")
        lbl.config(font=("Arial", 10))
        lbl.grid(row=1, column=0, columnspan=3)
        lbl = Label(self.window, text=" : - : - : - : - : - : - : - : - : - : - : - : ")
        lbl.config(font=("Arial", 25))
        lbl.grid(row=8, column=0, columnspan=3)
        btn = Button(self.window, text="Equation Solution", command=self.SolEcu)
        btn.grid(column=1, row=3)
        btn = Button(self.window, text="Interpolation", command=self.Inter)
        btn.grid(column=1, row=4)
        btn = Button(self.window, text="Evaluate/f(x)", command=self.Eval)
        btn.grid(column=1, row=2)
        btn = Button(self.window, text="Differentiation", command=self.Diff)
        btn.grid(column=1, row=5)
        self.window.mainloop()

    def SolEcu(self):
        SolEcuaciones()

    def Eval(self):
        def clicked():
            try:
                txt.delete(1.0, END)
                if fx.get() == "" or it.get() == "":
                    txt.insert(INSERT, "Missing data")
                    return
                x = it.get().split(",")
                r = ""
                for i in x:
                    res = Funcion(fx.get(), i)
                    r += res.Calculate()+"\n"
                txt.insert(INSERT, r)
            except SyntaxError:
                txt.insert(INSERT, "Syntax error")
            except ValueError:
                txt.insert(INSERT, "Domain error, Value error")
        window = Tk()
        window.title("Evaluate/f(x)")
        window.iconbitmap('Suma.ico')
        window.geometry("450x450")
        window.resizable(width=False, height=False)
        menu = Menu(window)
        panel = PanedWindow(window)
        lbl = Label(panel, text="f(x):")
        lbl.grid(column=1, row=1)
        lbl = Label(panel, text="x:")
        lbl.grid(column=1, row=2)
        fx = Entry(panel, width=20)
        fx.grid(column=2, row=1)
        it = Entry(panel, width=20)
        it.grid(column=2, row=2)
        btn = Button(panel, text="Evaluate", command=clicked)
        btn.grid(column=2, row=4)
        txt = scrolledtext.ScrolledText(window, width=55, height=21)
        txt.grid(column=0, row=1)
        panel.grid(column=0, row=0)
        menu.add_cascade(label='Documentation', command=self.Doc)
        menu.add_cascade(label='Help', command=self.aiuda)
        window.config(menu=menu)
        window.mainloop()

    def Inter(self):
        Interpolacion()

    def Diff(self):
        Differ()

    def aiuda(self):
        text = "Operations: \n" \
               "(+) Addition _ (-) Subtract _ (/) Division _ (*) ​​Multiplication \n" \
               "(**) Power _ math.sqrt() Square root \n" \
               "Documentation: \n Learn to use more functions from the math library \n" \
               "math.sin (), math.cos (), math.tan(), math.log (), math.exp () \n" \
               "Tips: \n" \
               "> Write 2x by typing 2*x don't forget the * operator \n" \
               "> Be sure to fill in all fields \n" \
               "> Intervals are in a, b format \n" \
               "> Place the parentheses correctly when writing your function"
        messagebox.showinfo('Help ??', text)

    def Doc(self):
        import webbrowser
        webbrowser.open("https://docs.python.org/3/library/math.html")



