from tkinter import *
from random import randint

root = Tk()
root.geometry("500x600")
root.resizable(0, 0)
root.configure(bg="#575757")

square_1_enable = 0
square_2_enable = 0
square_3_enable = 0
square_4_enable = 0
square_5_enable = 0
square_6_enable = 0
square_7_enable = 0
square_8_enable = 0
square_9_enable = 0

square_enable = [
    square_1_enable,
    square_2_enable, square_3_enable,
    square_4_enable, square_5_enable,
    square_6_enable, square_7_enable,
    square_8_enable, square_9_enable]


def random_square():
    random_number = randint(1, 9)


    while True:
        if random_number == 1:
            if square_1_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 2:
            if square_2_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 3:
            if square_3_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 4:
            if square_4_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 5:
            if square_5_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 6:
            if square_6_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 7:
            if square_7_enable in square_enable:
                print("a")
                break
            else:
                continue
        elif random_number == 8:
            if square_2_enable in square_enable:
                print("8")
                break
            else:
                continue
        elif random_number == 9:
            if square_2_enable in square_enable:
                print("9")
                break
            else:
                continue

def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''

def button_enable_check():
    if square_1["state"] == DISABLED:
        square_enable.pop(square_1_enable)
    elif square_2["state"] == DISABLED:
        square_enable.pop(square_2_enable)
    elif square_3["state"] == DISABLED:
        square_enable.pop(square_3_enable)
    elif square_4["state"] == DISABLED:
        square_enable.pop(square_4_enable)
    elif square_5["state"] == DISABLED:
        square_enable.pop(square_5_enable)
    elif square_6["state"] == DISABLED:
        square_enable.pop(square_6_enable)
    elif square_7["state"] == DISABLED:
        square_enable.pop(square_7_enable)
    elif square_8["state"] == DISABLED:
        square_enable.pop(square_8_enable)
    elif square_9["state"] == DISABLED:
        square_enable.pop(square_9_enable)

def disable_every_button():
    square_2.configure(state=DISABLED)
    square_3.configure(state=DISABLED)
    square_4.configure(state=DISABLED)
    square_5.configure(state=DISABLED)
    square_6.configure(state=DISABLED)
    square_7.configure(state=DISABLED)
    square_8.configure(state=DISABLED)
    square_9.configure(state=DISABLED)



def button_click(num):


    if num == 1:
        square_1.configure(image=cross_image, height=165, width=160, state=DISABLED)
        tksleep(3)
        button_enable_check()


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
