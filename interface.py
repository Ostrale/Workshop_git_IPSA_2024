"""
Cette branche coresponds au dévelopment de l'interface graphique Tkinter. 

Authors 

"""

import tkinter as tk 

fenetre = tk.Tk()
fenetre.title("interface")
fenetre.geometry("400x300")
fenetre.configure(bg="#49A")

label = tk.Label(fenetre, text="Variateur angle : ", font=("Helvetica 15 bold"))
label.pack()

btn = tk.Button(fenetre, text="move", font=("Helvetica 12 bold"), cursor="pirate").pack()

fenetre.mainloop()


