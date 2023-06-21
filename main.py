from tkinter import *

root = Tk()
root.geometry("500x600")
root.resizable(0, 0)
root.configure(bg="#575757")

overlay_image = PhotoImage(file = r"overlay.png")

overlay = Label(root, image=overlay_image, bg="#575757", fg="#575757", borderwidth=0)
overlay.pack()

root.mainloop()