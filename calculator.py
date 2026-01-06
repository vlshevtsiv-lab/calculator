import tkinter as tk

current_expression = ""

def on_button_click(text):
    global current_expression
    if text == "C":
        current_expression = ""
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            result = str(eval(current_expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            current_expression = result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            current_expression + ""
    else:
        current_expression += text
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_expression)







def set_theme(theme_name):
    themes = {
        "Світла": {"bg": "#FFFFFF", "fg": "#000000", "button_bg": "#F0F0F0", "button_fg": "#000000"},
        "Темна": {"bg": "#333333", "fg": "#FFFFFF", "button_bg": "#555555", "button_fg": "#FFFFFF"},
        "Синя": {"bg": "#E0F7FA", "fg": "#01579B", "button_bg": "#B3E5FC", "button_fg": "#01579B"},
        "Зелена": {"bg": "#E8F5E8", "fg": "#2E7D32", "button_bg": "#C8E6C9", "button_fg": "#2E7D32"},
        "Червона": {"bg": "#FFEBEE", "fg": "#B71C1C", "button_bg": "#FFCDD2", "button_fg": "#B71C1C"}
    }
    theme = themes.get(theme_name, themes ["Світла"])
    root.config(bg=theme["bg"])
    entry.config(bg=theme["bg"], fg=theme["fg"])
    for button in buttons:
        button.config(bg=theme["button_bg"], fg=theme["button_fg"])

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")

entry = tk.Entry(root, font=('Arial', 24), justify='right')
entry.pack(fill=tk.X, padx=10, pady=10)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "*",
    "0", "C", "=", "+"
]

buttons = []
frame = tk.Frame(root)
frame.pack()

for i, text in enumerate(button_texts):
    button = tk.Button(frame, text=text, font=("Arial", 18), command=lambda t=text: on_button_click(t))
    button.grid(row=1//4, column=1%4, sticky="nsew", padx=5, pady=5)
    buttons.append(button)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

menubar = tk.Menu(root, tearoff=0)
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command (label="Світла", command=lambda: set_theme( "Світла"))
settings_menu.add_command(label="Темна", command=lambda: set_theme( "Темна"))
settings_menu.add_command (label="Синя", command=lambda: set_theme("Синя"))
settings_menu.add_command (label="Зелена", command=lambda: set_theme ("Зелена"))
settings_menu.add_command (label="Червона", command=lambda: set_theme ("Червона"))
menubar.add_cascade(label="Налаштування", menu=settings_menu)
root.config(menu=menubar)

set_theme("Світла")

root.mainloop()