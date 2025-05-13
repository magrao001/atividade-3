import tkinter as tk 

def press(key): 

    current = display.get()

    if key == '=': 

        try: 
            result = str(eval(current)) 
            display.set(result)
        except Exception: 
            display.set("ERROR")
    elif key == 'C': 
        display.set("") 
    else: 
        display.set(current + key) 


root = tk.Tk() 
root.title("Calculadora") 
root.geometry("425x550") 
root.config(bg="white"
root.option_add("*Font", ("Courier New", 20)) 


display = tk.StringVar() 
display_label = tk.Label(root, textvariable=display, height=2, width=20, bg="white", fg="black", anchor="e", font=("Courier New", 24)) 
display_label.grid(row=0, column=0, columnspan=4) 


button_style = { 

    "width": 5, 
    "height": 2, 
    "fg": "white", 
    "bg": "black", 
    "font": ("Courier New", 20), 
    "relief": "raised",
    "bd": 4 

} 
 

buttons = [ 

    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), 
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3), 
    ('(', 5, 0), (')', 5, 1), ('^', 5, 2), ('=', 5, 3) 

] 


def button_pressed(key): 

    press(key) 


for (text, row, col) in buttons: 

    button = tk.Button(root, text=text, **button_style, command=lambda key=text: button_pressed(key)) 

    button.grid(row=row, column=col, padx=5, pady=5) 

 
root.mainloop() 