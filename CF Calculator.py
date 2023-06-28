from tkinter import *

root = Tk()
root.title("Cyber Father Calculator")
f_num = ""
# root.geometry("400x500+100+100")

#                                           FUNCTIONS
#######################################################################################################################


def click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))


def clear():
    display.delete(0, END)


def add():
    first_no = display.get()
    global f_num
    f_num = int(first_no)
    display.delete(0, END)


def equal():
    second_no = display.get()
    display.delete(0, END)
    display.insert(0, f_num + int(second_no))


def subtract():
    return


def multiply():
    return


def divide():
    return


#######################################################################################################################
#######################################################################################################################

#                                           CREATING WIDGETS

#   ENTRY
display = Entry(root, width=45, borderwidth=4)

#   BUTTONS
# Operators
button_add = Button(root, text="+", padx=30, pady=52, command=add)
button_subtract = Button(root, text="-", padx=39, pady=20, command=subtract)
button_multiply = Button(root, text="x", padx=38, pady=20, command=multiply)
button_divide = Button(root, text="÷", padx=37, pady=20, command=divide)

# Others
button_sqrt = Button(root, text="√x", padx=36, pady=20, command=lambda: click(0))   # Square root
button_dp = Button(root, text=".", padx=42, pady=20, command=lambda: click(0))      # Decimal point
button_equal = Button(root, text="=", padx=30, pady=52, command=equal)
button_clear = Button(root, text="Clear", padx=28, pady=20, command=clear)

# Numbers
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

# Scientific functions
button_CE = Button(root, text="CE", padx=35, pady=20, command=add)              # CE
button_C = Button(root, text="C", padx=39, pady=20, command=add)                # Clear
button_log = Button(root, text="log", padx=34, pady=20, command=add)            # Logarithm
button_pi = Button(root, text="π", padx=38, pady=20, command=add)               # Pi constant
button_del = Button(root, text="BKSP", padx=20, pady=20, command=add)           # Delete
button_LP = Button(root, text="(", padx=40, pady=20, command=add)               # Left parentheses
button_RP = Button(root, text=")", padx=40, pady=20, command=add)               # Right parentheses
button_cos = Button(root, text="cos", padx=31, pady=20, command=add)            # Angle COS
button_sin = Button(root, text="sin", padx=34, pady=20, command=add)            # Angle SIN
button_tan = Button(root, text="tan", padx=24, pady=20, command=add)            # Angle TAN
button_cmp = Button(root, text="==", padx=82, pady=20, command=add)             # Comparison(==)
button_tmp = Button(root, text="°C to °F", padx=20, pady=20, command=add)       # Temperature
button_dst = Button(root, text="m to km", padx=19, pady=20, command=add)        # Distance conversion
button_mod = Button(root, text="mod", padx=21, pady=20, command=add)            # Modulo

# Frames
separator = LabelFrame(root, width=500, height=100)


#######################################################################################################################
#######################################################################################################################

#                                           APPLYING WIDGETS


#   ENTRY
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# ROW 1
button_CE.grid(row=1, column=0)
button_C.grid(row=1, column=1)
button_log.grid(row=1, column=2)
button_pi.grid(row=1, column=3)
button_del.grid(row=1, column=4)

# ROW 2
button_LP.grid(row=2, column=0)
button_RP.grid(row=2, column=1)
button_cos.grid(row=2, column=2)
button_sin.grid(row=2, column=3)
button_tan.grid(row=2, column=4)

# ROW 3
button_cmp.grid(row=3, column=0, columnspan=2)
button_tmp.grid(row=3, column=2)
button_dst.grid(row=3, column=3)
button_mod.grid(row=3, column=4)

# ROW 4
# separator.grid(row=4, column=0, columnspan=4)

#    BUTTONS
# ROW 7
button_1.grid(row=7, column=0)
button_2.grid(row=7, column=1)
button_3.grid(row=7, column=2)
button_multiply.grid(row=7, column=3)
button_equal.grid(row=7, column=4, rowspan=2)

# ROW 6
button_4.grid(row=6, column=0)
button_5.grid(row=6, column=1)
button_6.grid(row=6, column=2)
button_subtract.grid(row=6, column=3)

# ROW 5
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_add.grid(row=5, column=4, rowspan=2)
button_clear.grid(row=5, column=3)

# ROW 8
button_sqrt.grid(row=8, column=0)
button_0.grid(row=8, column=1)
button_dp.grid(row=8, column=2)
button_divide.grid(row=8, column=3)




#######################################################################################################################
#######################################################################################################################

# MAINLOOP
root.mainloop()
