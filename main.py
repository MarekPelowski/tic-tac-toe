from tkinter import *

root = Tk()
root.geometry("500x600")
root.resizable(0, 0)
root.configure(bg="#575757")

def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''

def button_click(num):
    if num == 1:
        square_1.configure(image=cross_image, height=165, width=160, state=DISABLED)
    elif num == 2:
        square_2.configure(image=cross_image, height=165, width=150, state=DISABLED)
    elif num == 3:
        square_3.configure(image=cross_image, height=165, width=160, state=DISABLED)
    elif num == 4:
        square_4.configure(image=cross_image, height=140, width=160, state=DISABLED)
    elif num == 5:
        square_5.configure(image=cross_image, height=140, width=150, state=DISABLED)
    elif num == 6:
        square_6.configure(image=cross_image, height=140, width=160, state=DISABLED)
    elif num == 7:
        square_7.configure(image=cross_image, height=155, width=160, state=DISABLED)
    elif num == 8:
        square_8.configure(image=cross_image, height=155, width=150, state=DISABLED)
    elif num == 9:
        square_9.configure(image=cross_image, height=155, width=160, state=DISABLED)


overlay_image = PhotoImage(file=r"overlay.png")
cross_image = PhotoImage(file=r"cross.png")
circle_image = PhotoImage(file=r"circle.png")

overlay = Label(root, image=overlay_image, bg="#575757", fg="#575757", borderwidth=0)
overlay.pack()

square_1 = Button(root, height=10, width=22, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(1))
square_1.place(x=0, y=0)

square_2 = Button(root, height=10, width=20, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(2))
square_2.place(x=173, y=0)

square_3 = Button(root, height=10, width=24, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(3))
square_3.place(x=334, y=0)

square_4 = Button(root, height=9, width=22, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(4))
square_4.place(x=0, y=175)

square_5 = Button(root, height=9, width=20, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(5))
square_5.place(x=173, y=175)

square_6 = Button(root, height=9, width=24, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(6))
square_6.place(x=334, y=175)

square_7 = Button(root, height=10, width=22, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(7))
square_7.place(x=0, y=335)

square_8 = Button(root, height=10, width=20, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(8))
square_8.place(x=173, y=335)

square_9 = Button(root, height=10, width=24, bg="#575757", fg="#575757", borderwidth=0, command=lambda: button_click(9))
square_9.place(x=334, y=335)


root.mainloop()
