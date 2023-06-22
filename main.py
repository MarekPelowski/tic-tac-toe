from tkinter import *

root = Tk()
root.geometry("500x600")
root.resizable(0, 0)
root.configure(bg="#575757")

overlay_image = PhotoImage(file=r"overlay.png")
cross_image = PhotoImage(file=r"cross.png")
circle_image = PhotoImage(file=r"circle.png")

overlay = Label(root, image=overlay_image, bg="#575757", fg="#575757", borderwidth=0)
overlay.pack()

square_1 = Button(root, height=10, width=22, bg="#575757", fg="#575757", borderwidth=0)
square_1.place(x=0, y=0)

square_2 = Button(root)
square_2.place()

square_3 = Button(root)
square_3.place()

square_4 = Button(root)
square_4.place()

square_5 = Button(root)
square_5.place()

square_6 = Button(root)
square_6.place()

square_7 = Button(root)
square_7.place()

square_8 = Button(root)
square_8.place()

square_9 = Button(root)
square_9.place()


root.mainloop()
