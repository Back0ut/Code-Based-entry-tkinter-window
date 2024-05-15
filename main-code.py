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

code = GenerateCode(6)
print(f'Your code is {code.code}')

window = tk.Tk()
window.title('Rooms')

label = tk.Label(window, text='')
label.pack()

def check_code(event):
    entered_code = entry.get()
    if entered_code == code.code:
        label.config(text='You entered!')
    elif entered_code == "command=<'re'>":
        code.re_generate()
        print(f'Your new code is {code.code}')
        label.config(text='Code regenerated. Enter the new code.')
    else:
        label.config(text='Error! Not a valid code.')

entry = tk.Entry(window)
entry.pack()
entry.bind('<Return>', check_code)

window.mainloop()
