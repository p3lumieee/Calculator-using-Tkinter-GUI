from tkinter import *

root = Tk()
root.title("Joan's Trade Calculator")

#                                                    functions
#######################################################################################################################
def button0_clk():
    hello = "Hello" + entry0.get()
    label0 = Label(root, text=hello)
    label0.pack()
#######################################################################################################################

#                                                     creating the widgets
#######################################################################################################################
# labels
label0 = Label(root, text="Hello World!")
label1 = Label(root, text="Welcome to Tkinter")

# buttons
button0 = Button(root, text="Enter your name: ", padx=10, pady=15, command=button0_clk, fg="blue")

# entry
entry0 = Entry(root, width=50)
#######################################################################################################################

#                                                     applying widgets
#######################################################################################################################
# label
label0.pack()
label1.pack()

# buttons
button0.pack()

# entry
entry0.pack()
entry0.insert(0, "Enter your name: ")
#######################################################################################################################

# the mainloop
root.mainloop()
