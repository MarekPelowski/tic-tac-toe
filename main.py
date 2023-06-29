from tkinter import *
from random import randint

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg="#575757")
root.title("tic tac toe")

circle_win_1 = False
circle_win_2 = False
circle_win_3 = False
circle_win_4 = False
circle_win_5 = False
circle_win_6 = False
circle_win_7 = False
circle_win_8 = False
circle_win_9 = False

cross_win_1 = False
cross_win_2 = False
cross_win_3 = False
cross_win_4 = False
cross_win_5 = False
cross_win_6 = False
cross_win_7 = False
cross_win_8 = False
cross_win_9 = False

square_1_enable = True
square_2_enable = True
square_3_enable = True
square_4_enable = True
square_5_enable = True
square_6_enable = True
square_7_enable = True
square_8_enable = True
square_9_enable = True

counter = 0


cross_win = [
    square_1_enable,
    square_2_enable, square_3_enable,
    square_4_enable, square_5_enable,
    square_6_enable, square_7_enable,
    square_8_enable, square_9_enable]

square_enable = [
    square_1_enable,
    square_2_enable, square_3_enable,
    square_4_enable, square_5_enable,
    square_6_enable, square_7_enable,
    square_8_enable, square_9_enable]


def win_circle_func():
    if circle_win_1 == True and circle_win_2 == True and circle_win_3 == True:
        print("circle wins")

    elif circle_win_1 == True and circle_win_4 == True and circle_win_7 == True:
        print("circle wins")

    elif circle_win_3 == True and circle_win_6 == True and circle_win_9 == True:
        print("circle wins")

    elif circle_win_7 == True and circle_win_8 == True and circle_win_9 == True:
        print("circle wins")

    elif circle_win_2 == True and circle_win_5 == True and circle_win_8 == True:
        print("circle wins")

    elif circle_win_4 == True and circle_win_5 == True and circle_win_6 == True:
        print("circle wins")

    elif circle_win_1 == True and circle_win_5 == True and circle_win_9  == True:
        print("circle wins")

    elif circle_win_3 == True and circle_win_5 == True and circle_win_7 == True:
        print("circle wins")

def win_cross_func():
    if cross_win_1 == True and cross_win_2 == True and cross_win_3 == True:
        print("cross wins")

    elif cross_win_1 == True and cross_win_4 == True and cross_win_7 == True:
        print("cross wins")

    elif cross_win_3 == True and cross_win_6 == True and cross_win_9 == True:
        print("cross wins")

    elif cross_win_7 == True and cross_win_8 == True and cross_win_9 == True:
        print("cross wins")

    elif cross_win_2 == True and cross_win_5 == True and cross_win_8 == True:
        print("cross wins")

    elif cross_win_4 == True and cross_win_5 == True and cross_win_6 == True:
        print("cross wins")

    elif cross_win_1 == True and cross_win_5 == True and cross_win_9  == True:
        print("cross wins")

    elif cross_win_3 == True and cross_win_5 == True and cross_win_7 == True:
        print("cross wins")

def counter_function():
    if counter == 4:

        if square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == True:
            square_9.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == True and square_9_enable == False:
            square_8.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == True and square_8_enable == False and square_9_enable == False:
            square_7.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == True and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_6.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == True and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_5.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == False and square_4_enable == True and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_4.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == False and square_3_enable == True and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_3.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == False and square_2_enable == True and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_2.configure(image=circle_image, height=165, width=160, state=DISABLED)

        elif square_1_enable == True and square_2_enable == False and square_3_enable == False and square_4_enable == False and square_5_enable == False and square_6_enable == False and square_7_enable == False and square_8_enable == False and square_9_enable == False:
            square_1.configure(image=circle_image, height=165, width=160, state=DISABLED)

def tksleep(t):
    ms = int(t+1000)
    var = IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
    '''
    from the internet
    '''

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
    global cross_win_1, cross_win_2, cross_win_3, cross_win_4, cross_win_5, cross_win_6, cross_win_7, cross_win_8, cross_win_9,\
        cross_win_1, square_1_enable, square_2_enable, square_3_enable, square_4_enable, square_5_enable, square_6_enable,\
        square_7_enable, square_8_enable, square_9_enable

    if num == 1:
        square_1.configure(image=cross_image, height=165, width=160, state=DISABLED)
        square_1_enable = False
        random_square()
        cross_win_1 = True
        win_cross_func()
        win_circle_func()

    elif num == 2:
        square_2.configure(image=cross_image, height=165, width=150, state=DISABLED)
        square_2_enable = False
        random_square()
        cross_win_2 = True
        win_cross_func()
        win_circle_func()

    elif num == 3:
        square_3.configure(image=cross_image, height=165, width=160, state=DISABLED)
        square_3_enable = False
        random_square()
        cross_win_3 = True
        win_cross_func()
        win_circle_func()

    elif num == 4:
        square_4.configure(image=cross_image, height=140, width=160, state=DISABLED)
        square_4_enable = False
        random_square()
        cross_win_4 = True
        win_cross_func()
        win_circle_func()


    elif num == 5:
        square_5.configure(image=cross_image, height=140, width=150, state=DISABLED)
        square_5_enable = False
        random_square()
        cross_win_5 = True
        win_cross_func()
        win_circle_func()

    elif num == 6:
        square_6.configure(image=cross_image, height=140, width=160, state=DISABLED)
        square_6_enable = False
        random_square()
        cross_win_6 = True
        win_cross_func()
        win_circle_func()

    elif num == 7:
        square_7.configure(image=cross_image, height=155, width=160, state=DISABLED)
        square_7_enable = False
        random_square()
        cross_win_7 = True
        win_cross_func()
        win_circle_func()

    elif num == 8:
        square_8.configure(image=cross_image, height=155, width=150, state=DISABLED)
        square_8_enable = False
        random_square()
        cross_win_8 = True
        win_cross_func()
        win_circle_func()

    elif num == 9:
        square_9.configure(image=cross_image, height=155, width=160, state=DISABLED)
        square_9_enable = False
        random_square()
        cross_win_9 = True
        win_cross_func()
        win_circle_func()


def random_square():
    global circle_win_1, circle_win_2, circle_win_3, circle_win_4, circle_win_5, circle_win_6, circle_win_7, circle_win_8, circle_win_9,\
        counter, square_1_enable, square_2_enable, square_3_enable, square_4_enable, square_5_enable, square_6_enable, square_7_enable,\
        square_8_enable, square_9_enable


    while True:
        random_number = randint(1, 9)

        if random_number == 1:
            if square_1_enable == True:
                counter = counter + 1
                square_1.configure(image=circle_image, height=165, width=160, state=DISABLED)
                square_1_enable = False
                circle_win_1 = True
                win_cross_func()
                win_circle_func()
                break

        elif random_number == 1:
            if square_1_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 2:
            if square_2_enable == True:
                counter = counter + 1
                square_2.configure(image=circle_image, height=165, width=150, state=DISABLED)
                square_2_enable = False
                circle_win_2 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 2:
            if square_2_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 3:
            if square_3_enable == True:
                counter = counter + 1
                square_3.configure(image=circle_image, height=165, width=160, state=DISABLED)
                square_3_enable = False
                circle_win_3 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 3:
            if square_3_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 4:
            if square_4_enable == True:
                counter = counter + 1
                square_4.configure(image=circle_image, height=140, width=160, state=DISABLED)
                square_4_enable = False
                circle_win_4 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 4:
            if square_4_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 5:
            if square_5_enable == True:
                counter = counter + 1
                square_5.configure(image=circle_image, height=140, width=150, state=DISABLED)
                square_5_enable = False
                circle_win_5 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 5:
            if square_5_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 6:
            if square_6_enable == True:
                counter = counter + 1
                square_6.configure(image=circle_image, height=140, width=160, state=DISABLED)
                square_6_enable = False
                circle_win_6 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 6:
            if square_6_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 7:
            if square_7_enable == True:
                counter = counter + 1
                square_7.configure(image=circle_image, height=155, width=160, state=DISABLED)
                square_7_enable = False
                circle_win_7 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number > 7:
            if square_7_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 8:
            if square_8_enable == True:
                counter = counter + 1
                square_8.configure(image=circle_image, height=155, width=150, state=DISABLED)
                square_8_enable = False
                circle_win_8 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number > 8:
            if square_8_enable == False:
                if counter == 4:
                    break
                else:
                    continue


        if random_number == 9:
            if square_9_enable == True:
                counter = counter + 1
                square_9.configure(image=circle_image, height=155, width=160, state=DISABLED)
                square_9_enable = False
                circle_win_9 = True
                win_cross_func()
                win_circle_func()
                break
        elif random_number == 9:

            if square_9_enable == False:
                if counter == 4:
                    break
                else:
                    continue

overlay_image = PhotoImage(file=r"overlay.png")
cross_image = PhotoImage(file=r"cross.png")
circle_image = PhotoImage(file=r"circle.png")
horizontal_line_image = PhotoImage(file=r"horizontal_line.png")
vertical_line_image = PhotoImage(file=r"vertical_line.png")

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

if square_1["state"] == DISABLED:
    square_1_enable = False

elif square_2["state"] == DISABLED:
    square_2_enable = False

elif square_3["state"] == DISABLED:
    square_3_enable = False

elif square_4["state"] == DISABLED:
    square_4_enable = False

elif square_5["state"] == DISABLED:
    square_5_enable = False

elif square_6["state"] == DISABLED:
    square_6_enable = False

elif square_7["state"] == DISABLED:
    square_7_enable = False

elif square_8["state"] == DISABLED:
    square_8_enable = False

elif square_9["state"] == DISABLED:
    square_9_enable = False

# horizontal_line = Label(image=horizontal_line_image, borderwidth=0)
# horizontal_line.place(x=20, y=60)
#
# horizontal_line = Label(image=horizontal_line_image, borderwidth=0)
# horizontal_line.place(x=20, y=225)
#
# horizontal_line = Label(image=horizontal_line_image, borderwidth=0)
# horizontal_line.place(x=20, y=390)
#
#
# vertical_line = Label(image=vertical_line_image, borderwidth=0)
# vertical_line.place(x=60, y=20)
#
# vertical_line = Label(image=vertical_line_image, borderwidth=0)
# vertical_line.place(x=225, y=20)
#
# vertical_line = Label(image=vertical_line_image, borderwidth=0)
# vertical_line.place(x=390, y=20)


root.mainloop()
