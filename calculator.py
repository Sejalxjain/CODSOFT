from tkinter import *

# Globally declare the expression variable
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to clear the last character in the expression
def clear_entry():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Function to clear the entire expression
def clear():
    global expression
    expression = ""
    equation.set("")
    result.set("")

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        result.set(total)
        expression = ""
    except:
        equation.set("Error")
        result.set("Error")
        expression = ""

# Create a GUI window
gui = Tk()
gui.title("Enhanced Calculator")

# Set the configuration of the GUI window
gui.geometry("400x500")
gui.configure(bg="black")

# StringVar() for the text entry box and result label
equation = StringVar()
result = StringVar()

# Create the text entry box for showing the expression
entry_field = Entry(gui, textvariable=equation, font=('Helvetica', 20))
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Create and configure buttons
button_config = {'fg': 'black', 'bg': 'gray', 'font': ('Helvetica', 18), 'height': 2, 'width': 8}

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

row_val = 1
col_val = 0

for button in buttons:
    Button(gui, text=button, command=lambda b=button: press(b) if b != '=' else equalpress(), **button_config).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear entry and clear buttons
Button(gui, text='CE', command=clear_entry, **button_config).grid(row=5, column=0)
Button(gui, text='C', command=clear, **button_config).grid(row=5, column=1)

# Result label
result_label = Label(gui, textvariable=result, font=('Helvetica', 20), fg="blue")
result_label.grid(row=6, column=0, columnspan=4)

# Bind numeric keys and operators to functions
for key in '0123456789+-*/.':
    gui.bind(key, lambda event, key=key: press(key) if key != '=' else equalpress())

# Start the GUI
gui.mainloop()
