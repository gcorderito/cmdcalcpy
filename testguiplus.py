import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_entry = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Pantalla de resultados
        result_display = tk.Entry(self.root, textvariable=self.result, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify=tk.RIGHT)
        result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Números y operadores
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 16), bd=5, relief=tk.GROOVE, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Establecer el mismo peso para todas las celdas para que los botones se expandan con el tamaño de la ventana
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == 'C':
            self.current_entry.set('')
            self.result.set('')
        elif text == '=':
            try:
                expression = self.current_entry.get()
                result = eval(expression)
                self.result.set(result)
            except Exception:
                self.result.set("Error")
        else:
            self.current_entry.set(self.current_entry.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
