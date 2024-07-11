import csv
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def elegir_archivo():
    global archivo_path
    archivo_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo_path:
        archivo_label.config(text=f"Archivo seleccionado: {archivo_path}")
        opciones_frame.pack()

def modificar_archivo():
    with open(archivo_path, 'r', newline='') as file_in, open(archivo_path, 'w', newline='') as file_out:
        reader = csv.reader(file_in, delimiter=',')
        writer = csv.writer(file_out, delimiter=';')
        writer.writerows(reader)
    messagebox.showinfo("Operación Exitosa", "El archivo original ha sido modificado correctamente.")
    reiniciar()

def guardar_como():
    new_name = simpledialog.askstring("Nuevo nombre", "Ingrese el nuevo nombre del archivo:")
    if new_name:
        folder_path = filedialog.askdirectory()
        if folder_path:
            new_file_path = f"{folder_path}/{new_name}.csv"
            with open(archivo_path, 'r', newline='') as file_in, open(new_file_path, 'w', newline='') as file_out:
                reader = csv.reader(file_in, delimiter=',')
                writer = csv.writer(file_out, delimiter=';')
                writer.writerows(reader)
            messagebox.showinfo("Operación Exitosa", f"El archivo ha sido creado exitosamente en {new_file_path}")
    reiniciar()

def reiniciar():
    archivo_label.config(text="No se ha seleccionado ningún archivo")
    opciones_frame.pack_forget()

root = tk.Tk()
root.title("CSV Delimiter Changer")
root.geometry("400x200")

archivo_path = ''

archivo_frame = tk.Frame(root)
archivo_frame.pack(pady=20)

archivo_label = tk.Label(archivo_frame, text="No se ha seleccionado ningún archivo")
archivo_label.pack()

buscar_btn = tk.Button(archivo_frame, text="Buscar Archivo CSV", command=elegir_archivo)
buscar_btn.pack()

opciones_frame = tk.Frame(root)

modificar_btn = tk.Button(opciones_frame, text="Modificar Archivo Original", command=modificar_archivo)
modificar_btn.pack(side=tk.LEFT, padx=10)

guardar_btn = tk.Button(opciones_frame, text="Guardar como...", command=guardar_como)
guardar_btn.pack(side=tk.RIGHT, padx=10)

reiniciar_btn = tk.Button(root, text="Usar de nuevo", command=reiniciar)
reiniciar_btn.pack(pady=10)

root.mainloop()
