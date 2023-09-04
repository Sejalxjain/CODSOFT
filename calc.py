from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def clear_entry():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

gui = Tk()
gui.title("Simple Calculator")

gui.geometry("350x450")
gui.configure(bg="black")

equation = StringVar()

entry_field = Entry(gui, textvariable=equation, font=('Helvetica', 20))
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

button_config = {'fg': 'black', 'bg': 'gray', 'font': ('Helvetica', 18), 'height': 2, 'width': 8}

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(gui, text=button, command=lambda b=button: press(b) if b != '=' else equalpress(), **button_config).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

Button(gui, text='CE', command=clear_entry, **button_config).grid(row=5, column=0)
Button(gui, text='C', command=clear, **button_config).grid(row=5, column=1)

gui.mainloop()
