from Tkinter import *
import tkinter as tk
from tkinter.ttk import *

class Passwordchecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

   def initialize_user_interface(self):
       self.parent.geometry("400x400")
       self.parent.title("Pokeirmanos")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.button=tk.Button(self.parent,text="testa", command=self.PassCheck)
       self.button.pack()
       self.label=tk.Label(self.parent,text="Fala um pokemon ae")
       self.label.pack()

   def PassCheck(self):
       password = self.entry.get()
       if len(password)>=9 and len(password)<=12:
          self.label.config(text="Acertou miseravi")
       else:
          self.label.config(text="ERRROOUUU")
 
# creates a Tk() object
master = tk.Tk()
 
# sets the geometry of main
# root window
master.geometry("200x200")
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    #newWindow = tk.Toplevel(master)
    root = tk.Tk()
    run = Passwordchecker(root)
    root.mainloop()
 

class KnapsackPackage(object):
    """ Knapsack Package Data Class """
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost

class FractionalKnapsack(object):
    def knapsackGreProc(self, W, V, M, n):
        packs = []
        for i in range(n):
            packs.append(KnapsackPackage(W[i], V[i]))
        packs.sort(reverse=True)
        remain = M
        result = 0
        i = 0
        stopProc = False

        while not stopProc:
            if packs[i].weight <= remain:
                remain -= packs[i].weight
                result += packs[i].value
                print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)

            if packs[i].weight > remain:
                i += 1

            if i == n:
                stopProc = True

        print("Max Value: ", result)

if __name__ == "__main__":

    label = Label(master,
                text ="Welcome stranger...")
    
    label.pack(pady = 10)
    
    master.title('Mercador Medieval')
    # a button widget which will open a
    # new window on button click
    btn = Button(master,
                text ="Iniciar",
                command = openNewWindow)
    btn.pack(pady = 10)

    btn2 = Button(master,
                text ="Sair",
                command = quit)
    btn2.pack(pady = 20) 
    # mainloop, runs infinitely
    tk.mainloop()
    W = [15, 10, 2, 4]
    V = [30, 25, 2, 6]
    M = 37
    n = 4
    proc = FractionalKnapsack()
    proc.knapsackGreProc(W, V, M, n)