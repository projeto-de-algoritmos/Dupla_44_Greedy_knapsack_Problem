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
 
 
label = Label(master,
              text ="Welcome stranger...")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Iniciar",
             command = openNewWindow)
btn.pack(pady = 10)

btn2 = Button(master,
             text ="Sair",
             command = openNewWindow)
btn2.pack(pady = 20) 
# mainloop, runs infinitely
tk.mainloop()