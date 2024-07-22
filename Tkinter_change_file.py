import tkinter as tk
from tkinter import filedialog, ttk
from datetime import datetime

def function_to_change(file_paths, enclosure, input_separator, output_separator, selected_date):
    # Aquí iría la lógica para cambiar los archivos.
    # Esta es una función de ejemplo.
    print("Archivos seleccionados:", file_paths)
    print("Enclosure:", enclosure)
    print("Separador de entrada:", input_separator)
    print("Separador de salida:", output_separator)
    print("Fecha seleccionada:", selected_date)

def open_file_explorer():
    file_paths = filedialog.askopenfilenames(title="Seleccionar archivos")
    if file_paths:
        file_list.set(file_paths)
    else:
        file_list.set([])

def apply_changes():
    if not file_list.get():
        tk.messagebox.showerror("Error", "Debe seleccionar al menos un archivo.")
        return

    enclosure = enclosure_var.get()
    input_separator = input_separator_var.get()
    output_separator = output_separator_var.get()
    selected_date = f"{year_var.get()}-{month_var.get()}-{day_var.get()}"

    if not (enclosure and input_separator and output_separator and year_var.get() and month_var.get() and day_var.get()):
        tk.messagebox.showerror("Error", "Todos los campos deben ser seleccionados.")
        return

    function_to_change(file_list.get(), enclosure, input_separator, output_separator, selected_date)

root = tk.Tk()
root.title("Aplicación de Procesamiento de Archivos")

# Variables
file_list = tk.Variable()
enclosure_var = tk.StringVar(value="False")
input_separator_var = tk.StringVar()
output_separator_var = tk.StringVar()
year_var = tk.StringVar()
month_var = tk.StringVar()
day_var = tk.StringVar()

# Widgets
file_button = tk.Button(root, text="Seleccionar Archivos", command=open_file_explorer)
file_button.grid(row=0, column=0, padx=10, pady=10)

file_label = tk.Label(root, textvariable=file_list, wraplength=300)
file_label.grid(row=0, column=1, padx=10, pady=10)

enclosure_label = tk.Label(root, text="Left/Right Enclosure:")
enclosure_label.grid(row=1, column=0, padx=10, pady=10)

enclosure_options = ttk.Combobox(root, textvariable=enclosure_var)
enclosure_options['values'] = ("True", "False")
enclosure_options.grid(row=1, column=1, padx=10, pady=10)

input_separator_label = tk.Label(root, text="Separador de archivos seleccionados:")
input_separator_label.grid(row=2, column=0, padx=10, pady=10)

input_separator_options = ttk.Combobox(root, textvariable=input_separator_var)
input_separator_options['values'] = (",", ";", "|", "\t")
input_separator_options.grid(row=2, column=1, padx=10, pady=10)

output_separator_label = tk.Label(root, text="Separador de archivos que desea obtener:")
output_separator_label.grid(row=3, column=0, padx=10, pady=10)

output_separator_options = ttk.Combobox(root, textvariable=output_separator_var)
output_separator_options['values'] = (",", ";", "|", "\t")
output_separator_options.grid(row=3, column=1, padx=10, pady=10)

date_label = tk.Label(root, text="Fecha deseada (Año-Mes-Día):")
date_label.grid(row=4, column=0, padx=10, pady=10)

year_entry = tk.Entry(root, textvariable=year_var)
year_entry.grid(row=4, column=1, padx=5, pady=10, sticky="W")

month_entry = tk.Entry(root, textvariable=month_var)
month_entry.grid(row=4, column=1, padx=5, pady=10)

day_entry = tk.Entry(root, textvariable=day_var)
day_entry.grid(row=4, column=1, padx=5, pady=10, sticky="E")

apply_button = tk.Button(root, text="Aplicar Cambios", command=apply_changes)
apply_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
