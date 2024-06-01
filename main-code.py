import tkinter as tk
from string import ascii_uppercase, ascii_lowercase
from random import choice

class GenerateCode:
    def __init__(self, length):
        self.length = int(length)
        self.listed_code = []
        self.generate()

    def generate(self):
        for i in range(0, self.length):
            letters = [choice(ascii_lowercase), choice(ascii_uppercase)]
            self.listed_code.append(choice(letters))
            if (i + 1) % 3 == 0 and i != self.length - 1:
                self.listed_code.append('-')
        
        self.code = ''.join(self.listed_code)

    def re_generate(self):
        self.listed_code.clear()
        for i in range(0, self.length):
            letters = [choice(ascii_lowercase), choice(ascii_uppercase)]
            self.listed_code.append(choice(letters))
            if (i + 1) % 3 == 0 and i != self.length - 1:
                self.listed_code.append('-')
        
        self.code = ''.join(self.listed_code)
    
    def delete_code(self):
        self.listed_code.clear()

code = GenerateCode(6)
print(f'Your code is {code.code}')

window = tk.Tk()
window.title('Rooms')
window.geometry('250x200')


label = tk.Label(window, text='')
label.pack()

def check_code(_) -> None:
    entered_code = entry.get()
    
    if entered_code == code.code: label.config(text='You entered!')

    elif entered_code == "command=<'re'>" or entered_code == 'command=<"re">' or entered_code == 'reset.co' or entered_code == 'reset-code':
        code.re_generate()
        print(f'Your new code is {code.code}')
        label.config(text='Code regenerated. Enter the new code.')
    elif entered_code == 'del-code' or entered_code == 'del': code.delete_code
    else: label.config(text='Error! Not a valid code.')

entry = tk.Entry(window)
entry.pack()
entry.bind('<Return>', check_code)

window.mainloop()
