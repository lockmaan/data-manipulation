from tkinter import *

root = Tk()
root.title("Calculator")


def botton_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if operator == "+":
        e.insert(0, f_num + int(second_number))
    elif operator == "-":
        e.insert(0, f_num - int(second_number))
    elif operator == "x":
        e.insert(0, f_num * int(second_number))
    elif operator == "/":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global operator
    operator = "-"
    e.delete(0, END)
    return


def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global operator
    operator = "x"
    e.delete(0, END)
    return


def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global operator
    operator = "/"
    e.delete(0, END)
    return


e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
myButton_1 = Button(root, text="1", padx=50, pady=23,
                    command=lambda: botton_click(1))
myButton_2 = Button(root, text="2", padx=50, pady=23,
                    command=lambda: botton_click(2))
myButton_3 = Button(root, text="3", padx=50, pady=23,
                    command=lambda: botton_click(3))
myButton_4 = Button(root, text="4", padx=50, pady=23,
                    command=lambda: botton_click(4))
myButton_5 = Button(root, text="5", padx=50, pady=23,
                    command=lambda: botton_click(5))
myButton_6 = Button(root, text="6", padx=50, pady=23,
                    command=lambda: botton_click(6))
myButton_7 = Button(root, text="7", padx=50, pady=23,
                    command=lambda: botton_click(7))
myButton_8 = Button(root, text="8", padx=50, pady=23,
                    command=lambda: botton_click(8))
myButton_9 = Button(root, text="9", padx=50, pady=23,
                    command=lambda: botton_click(9))
myButton_0 = Button(root, text="0", padx=50, pady=23,
                    command=lambda: botton_click(0))
myButton_add = Button(root, text="+", padx=49, pady=23,
                      command=button_add)
myButton_equal = Button(root, text="=", padx=91, pady=23,
                        command=button_equal)
myButton_clear = Button(root, text="C", padx=90, pady=23,
                        command=button_clear)


myButton_subtract = Button(root, text="-", padx=50, pady=23,
                           command=button_subtract)
myButton_multiply = Button(root, text="x", padx=50, pady=23,
                           command=button_multiply)
myButton_divide = Button(root, text="/", padx=50, pady=23,
                         command=button_divide)

myButton_9.grid(row=1, column=2)
myButton_8.grid(row=1, column=1)
myButton_7.grid(row=1, column=0)

myButton_6.grid(row=2, column=2)
myButton_5.grid(row=2, column=1)
myButton_4.grid(row=2, column=0)

myButton_3.grid(row=3, column=2)
myButton_2.grid(row=3, column=1)
myButton_1.grid(row=3, column=0)

myButton_0.grid(row=4, column=0)

myButton_clear.grid(row=4, column=1, columnspan=2)
myButton_equal.grid(row=5, column=1, columnspan=2)
myButton_add.grid(row=5, column=0)

myButton_subtract.grid(row=6, column=0)
myButton_multiply.grid(row=6, column=1)
myButton_divide.grid(row=6, column=2)

root.mainloop()
