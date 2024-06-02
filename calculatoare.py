import math
import tkinter as tk
from tkinter import font




class AdvancedAnalogCalculator:
    def __init__(self):
        self.value = 0
        self.memory = 0
        self.current_input = ""

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x != 0:
            self.value /= x
        else:
            raise ValueError("Division by zero is not allowed")
        return self.value

    def sine(self):
        self.value = math.sin(math.radians(self.value))
        return self.value

    def cosine(self):
        self.value = math.cos(math.radians(self.value))
        return self.value

    def log(self):
        if self.value > 0:
            self.value = math.log(self.value)
        else:
            raise ValueError("Logarithm of non-positive value is not allowed")
        return self.value

    def exponential(self):
        self.value = math.exp(self.value)
        return self.value

    def reset(self):
        self.value = 0
        self.current_input = ""

    def get_value(self):
        return self.value


class CalculatorApp:
    def __init__(self, root):
        self.calc = AdvancedAnalogCalculator()
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)
        self.root.configure(bg='gray')
        self.create_widgets()
        self.current_op = None
        self.previous_value = 0

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Helvetica", 36), bd=10, insertwidth=2, width=14, borderwidth=4,
                                justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('ln', 1, 0, lambda: self.on_function_click('log'), 'lightblue'),
            ('sin', 1, 1, lambda: self.on_function_click('sin'), 'lightblue'),
            ('cos', 1, 2, lambda: self.on_function_click('cos'), 'lightblue'),
            ('/', 1, 3, lambda: self.set_operation('/'), 'orange'),
            ('7', 2, 0, lambda: self.on_button_click('7'), 'white'),
            ('8', 2, 1, lambda: self.on_button_click('8'), 'white'),
            ('9', 2, 2, lambda: self.on_button_click('9'), 'white'),
            ('*', 2, 3, lambda: self.set_operation('*'), 'orange'),
            ('4', 3, 0, lambda: self.on_button_click('4'), 'white'),
            ('5', 3, 1, lambda: self.on_button_click('5'), 'white'),
            ('6', 3, 2, lambda: self.on_button_click('6'), 'white'),
            ('-', 3, 3, lambda: self.set_operation('-'), 'orange'),
            ('1', 4, 0, lambda: self.on_button_click('1'), 'white'),
            ('2', 4, 1, lambda: self.on_button_click('2'), 'white'),
            ('3', 4, 2, lambda: self.on_button_click('3'), 'white'),
            ('+', 4, 3, lambda: self.set_operation('+'), 'orange'),
            ('0', 5, 0, lambda: self.on_button_click('0'), 'white'),
            ('.', 5, 1, lambda: self.on_button_click('.'), 'white'),
            ('=', 5, 2, self.calculate, 'orange'),
            ('C', 5, 3, self.clear, 'orange')
        ]

        for (text, row, col, cmd, color) in buttons:
            self.create_button(text, row, col, cmd, color)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col, cmd, color):
        button = tk.Button(self.root, text=text, font=("Helvetica", 24), bg=color, fg='black', command=cmd)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        self.display.insert(tk.END, char)

    def set_operation(self, op):
        self.current_op = op
        self.previous_value = float(self.display.get())
        self.display.delete(0, tk.END)

    def on_function_click(self, func):
        try:
            self.calc.value = float(self.display.get())
            if func == 'sin':
                self.calc.sine()
            elif func == 'cos':
                self.calc.cosine()
            elif func == 'log':
                self.calc.log()
            self.update_display()
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')

    def calculate(self):
        if self.current_op:
            try:
                current_value = float(self.display.get())
                if self.current_op == '+':
                    self.calc.value = self.previous_value + current_value
                elif self.current_op == '-':
                    self.calc.value = self.previous_value - current_value
                elif self.current_op == '*':
                    self.calc.value = self.previous_value * current_value
                elif self.current_op == '/':
                    if current_value == 0:
                        raise ValueError("Division by zero")
                    self.calc.value = self.previous_value / current_value
                self.update_display()
                self.current_op = None
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')

    def clear(self):
        self.calc.reset()
        self.display.delete(0, tk.END)

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, str(self.calc.get_value()))


class Soroban:
    def __init__(self, rods):
        self.rods = rods
        self.upper_beads = [0] * rods
        self.lower_beads = [0] * rods

    def move_bead_up(self, rod):
        if self.lower_beads[rod] < 4:
            self.lower_beads[rod] += 1

    def move_bead_down(self, rod):
        if self.lower_beads[rod] > 0:
            self.lower_beads[rod] -= 1

    def move_upper_bead(self, rod):
        self.upper_beads[rod] = 1 - self.upper_beads[rod]

    def calculate(self):
        total = 0
        for i in range(self.rods):
            total += (5 * self.upper_beads[i] + self.lower_beads[i]) * (10 ** (self.rods - i - 1))
        return total


class SorobanUI:
    def __init__(self, root, soroban):
        self.root = root
        self.soroban = soroban
        self.create_ui()

    def create_ui(self):
        self.canvas = tk.Canvas(self.root, width=500, height=600)
        self.canvas.pack()
        self.draw_soroban()
        self.root.bind('<Button-1>', self.handle_click)

    def draw_soroban(self):
        self.canvas.delete("all")

        for rod in range(self.soroban.rods):
            x = 50 + rod * 50  
            self.canvas.create_line(x, 15, x, 300, width=2)
            self.draw_beads(rod, x)
        self.canvas.create_rectangle(25, 90, 275, 100, outline='black', fill='#b5651d')
        self.canvas.create_rectangle(25, 290, 275, 300, outline='black', fill='#b5651d')
        self.canvas.create_rectangle(25, 10, 275, 20, outline='black', fill='#b5651d')
        self.canvas.create_rectangle(15, 10, 25, 300, outline='black', fill='#b5651d')
        self.canvas.create_rectangle(275, 10, 285, 300, outline='black', fill='#b5651d')



    def draw_beads(self, rod, x):
        if self.soroban.upper_beads[rod] == 1:
            self.canvas.create_oval(x - 10, 60, x + 10, 80, fill='red')
        else:
            self.canvas.create_oval(x - 10, 30, x + 10, 50, fill='red')

        for i in range(4):
            y = 150 + i * 30
            if i < self.soroban.lower_beads[rod]:
                y -= 40
            self.canvas.create_oval(x - 10, y, x + 10, y + 20, fill='black')

    def draw_number(self):
        number = self.soroban.calculate()
        self.canvas.create_text(180, 400, text='NUMAR CURENT:'+str(number), font=("Inlanders", 24, "bold"))
        self.canvas.create_text(300, 400, text=str(number), font=("Arial", 24, "bold"))
        
    def handle_click(self, event):
        if 40<=event.x<=60:
            rod=0
        elif  90<=event.x<=110:
            rod=1
        elif  140<=event.x<=160:
            rod=2
        elif  190<=event.x<=210:
            rod=3
        elif  240<=event.x<=260:
            rod=4
        if 30 <= event.y <= 80:
            self.soroban.move_upper_bead(rod)
        elif 150 <= event.y <= 300:
            if event.y % 30 < 15:
                self.soroban.move_bead_up(rod)
            else:
                self.soroban.move_bead_down(rod)
        self.draw_soroban()
        self.draw_number()
        print(f"Current value: {self.soroban.calculate()}  {event.x, event.y,rod}")


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.configure(bg='#3141c0')
        self.root.geometry("1000x600")
        self.root.resizable(False, False) 
        self.bg_image = tk.PhotoImage(file="img1.png")
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        
        exit_button = tk.Button(self.root, text="x", font=("Inlanders", 24), bg='#FF004F', fg='white',
                                command=self.root.quit)
        exit_button.pack(side="right", anchor="ne")

        title = tk.Label(self.root, text="Main Menu", font=("Inlanders", 36), bg='#090445', fg='white')

        title.pack(expand=True)
        
        open_calc_button = tk.Button(self.root, text="Calculator", font=("Inlanders", 36), bg='#E6E6FA',
                                     fg='black', command=self.open_calculator)
        open_calc_button.pack(expand=True)

        open_soroban_button = tk.Button(self.root, text="Soroban", font=("Inlanders", 36), bg='#E6E6FA',
                                        fg='black', command=self.open_soroban)
        open_soroban_button.pack(expand=True)

        

    def open_calculator(self):
        self.root.destroy()
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()

    def open_soroban(self):
        self.root.destroy()
        root = tk.Tk()
        root.title("Soroban Abacus")
        soroban = Soroban(rods=5)
        app = SorobanUI(root, soroban)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    
    menu = MainMenu(root)
    root.mainloop()
