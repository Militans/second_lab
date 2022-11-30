from tkinter import *
from tkinter import messagebox
from math import sqrt

root = Tk()
root['bg'] = "#007fff"
root.title("Калькулятор")
root.geometry("280x420+600+200")
root.resizable(False, False)


def Point():
    temp = calc.get()
    if temp.count(".") == 0:
        calc.delete(0, END)
        calc.insert(0, temp + '.')
    elif ('+' in temp or '-' in temp or '*' in temp or '/' in temp) and temp.count('.') <= 1:
        calc.delete(0, END)
        calc.insert(0, temp + '.')


def clear():
    calc.delete(0, END)
    calc.insert(0, '0')


def add_digit(value):
    temp = calc.get()
    if temp[0] == '0' and len(temp) == 1:
        temp = temp[1:]
    calc.delete(0, 'end')
    calc.insert(0, temp + value)


def add_operation(operation):
    temp = calc.get()
    if temp[-1] in '+-*/':
        temp = temp[:-1]
    elif '-' in operation or '+' in operation or '*' in operation or '/' in operation:
        calculate()
        temp = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, temp + operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showerror("Error!", "Деление на 0 невозможно!")
        calc.insert(0, "0")
    except (NameError, SyntaxError):
        messagebox.showerror("Error!", "Only digits or operations [+-*/]")
        calc.insert(0, "0")


def make_operation_button(operation):
    return Button(text=operation, bd=3, font=('Arial', 13), command=lambda: add_operation(operation), fg='red')


def make_clear_button(c):
    return Button(text=c, bd=3, font=('Arial', 13), command=clear, fg='red')


def make_digit_button(digit):
    return Button(text=digit, bd=3, font=("Arial", 13), command=lambda: add_digit(digit), fg='red')


def make_calculate_button(op):
    return Button(text=op, bd=3, font=("Arial", 13), command=calculate, fg='red')


def make_point_button(point):
    return Button(text=point, bd=3, font=("Arial", 13), command=Point, fg='red')


def sqrt_():
    temp = calc.get()
    if '-' in temp or '+' in temp or '*' in temp or '/' in temp:
        temp2 = eval(temp)
        calc.delete(0, END)
        try:
            calc.insert(0, str(sqrt(float(temp2))))
        except ValueError:
            messagebox.showerror("Error!", "You can't take a sqrt from the number lower 0")
            calc.insert(0, '0')
    else:
        calc.delete(0, END)
        calc.insert(0, str(sqrt(float(temp))))


calc = Entry(root, justify=RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=4, sticky='wens', padx=4, pady=4)
calc.insert(0, '0')


make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=4, pady=4)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=4, pady=4)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=4, pady=4)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=4, pady=4)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=4, pady=4)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=4, pady=4)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=4, pady=4)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=4, pady=4)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=4, pady=4)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=4, pady=4)


make_operation_button("+").grid(row=1, column=3, sticky='wens', padx=4, pady=4)
make_operation_button("-").grid(row=2, column=3, sticky='wens', padx=4, pady=4)
make_operation_button("*").grid(row=3, column=3, sticky='wens', padx=4, pady=4)
make_operation_button("/").grid(row=4, column=3, sticky='wens', padx=4, pady=4)
Button(text="√", bd=4, font=('Arial', 13), fg='red', command=sqrt_).grid(row=4, column=1, sticky='wens', padx=4, pady=4)
make_clear_button('C').grid(row=4, column=2, sticky='wens', padx=4, pady=4)
make_calculate_button('=').grid(row=5, column=0, columnspan=3, sticky='wens', padx=4, pady=4)
make_point_button('.').grid(row=5, column=3, sticky='wens', padx=4, pady=4)


for i in range(4):
    root.grid_columnconfigure(i, minsize=70)

for i in range(6):
    root.grid_rowconfigure(i, minsize=70)


root.mainloop()
