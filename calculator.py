import tkinter as tk


gui = tk.Tk()
gui.resizable(False, False)
gui.configure(bg='#141414')
gui.title("Calculator")
gui.geometry('530x800')
gui.iconbitmap('icon.ico')

equation = ""


def add(value):
    global equation

    if value == '.':
        if equation == "":
            equation += "0."
        elif equation[-1] != '.':
            equation += value
    else:
        equation += value

    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    equation = equation.replace('x', '*')

    curr_num = ""
    for i in equation:
        if i.isnumeric() or i == '.':
            curr_num += i
        elif i == '%':
            equation = equation.replace(curr_num + '%', str(float(curr_num) / 100))
        else:
            curr_num = ""

    result = ""
    if equation != "":
        try:
            result = eval(equation)
            if result - int(result) == 0:
                result = int(result)
        except:
            result = "Error"

    label_result.config(text=result)
    equation = str(result)


label_result = tk.Label(gui, width=25, height=3, text='', font=('monospace', 30), bg='#141414', fg='#FFF8F0',
                        anchor='e')
label_result.pack(padx=30)

btn_lbracket = tk.Button(gui, text='(', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                         bg='#474747', command=lambda: add('('))
btn_lbracket.place(x=20, y=140)
btn_rbracket = tk.Button(gui, text=')', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                         bg='#474747', command=lambda: add(')'))
btn_rbracket.place(x=150, y=140)
btn_perc = tk.Button(gui, text='%', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#474747',
                     command=lambda: add('%'))
btn_perc.place(x=280, y=140)
btn_div = tk.Button(gui, text='/', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#bb9d2f',
                    command=lambda: add('/'))
btn_div.place(x=410, y=140)

btn_seven = tk.Button(gui, text='7', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                      bg='#2d2d2d', command=lambda: add('7'))
btn_seven.place(x=20, y=270)
btn_eight = tk.Button(gui, text='8', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                      bg='#2d2d2d', command=lambda: add('8'))
btn_eight.place(x=150, y=270)
btn_nine = tk.Button(gui, text='9', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                     command=lambda: add('9'))
btn_nine.place(x=280, y=270)
btn_x = tk.Button(gui, text='x', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#bb9d2f',
                  command=lambda: add('x'))
btn_x.place(x=410, y=270)

btn_four = tk.Button(gui, text='4', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                     command=lambda: add('4'))
btn_four.place(x=20, y=400)
btn_five = tk.Button(gui, text='5', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                     command=lambda: add('5'))
btn_five.place(x=150, y=400)
btn_six = tk.Button(gui, text='6', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                    command=lambda: add('6'))
btn_six.place(x=280, y=400)
btn_minus = tk.Button(gui, text='-', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                      bg='#bb9d2f', command=lambda: add('-'))
btn_minus.place(x=410, y=400)

btn_one = tk.Button(gui, text='1', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                    command=lambda: add('1'))
btn_one.place(x=20, y=530)
btn_two = tk.Button(gui, text='2', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                    command=lambda: add('2'))
btn_two.place(x=150, y=530)
btn_three = tk.Button(gui, text='3', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                      bg='#2d2d2d', command=lambda: add('3'))
btn_three.place(x=280, y=530)
btn_plus = tk.Button(gui, text='+', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#bb9d2f',
                     command=lambda: add('+'))
btn_plus.place(x=410, y=530)

btn_dot = tk.Button(gui, text='.', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                    command=lambda: add('.'))
btn_dot.place(x=20, y=660)
btn_zero = tk.Button(gui, text='0', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                     command=lambda: add('0'))
btn_zero.place(x=150, y=660)
btn_c = tk.Button(gui, text='C', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0', bg='#2d2d2d',
                  command=lambda: clear())
btn_c.place(x=280, y=660)
btn_equals = tk.Button(gui, text='=', width=5, height=2, font=('monospace', 25), bd=0, fg='#FFF8F0',
                       bg='#bb9d2f', command=lambda: calculate())
btn_equals.place(x=410, y=660)

gui.mainloop()
