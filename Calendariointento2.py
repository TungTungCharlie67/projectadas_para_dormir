import tkinter as tk
from tkcalendar import Calendar
from datetime import date
import Tareas
import os
import csv
from tkinter import messagebox

hoy = date.today()

print(hoy)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "saver.csv")

def onetimereader():
    try:
        with open(file_path, "x") as file:
            print("file created")
    except FileExistsError:
        print("file exists")

    with open(file_path, "r") as file:
        content = csv.reader(file)
        for row in content:
                holder=Tareas.Tareas(
                row[0], 
                int(row[1]), 
                int(row[2]), 
                int(row[3]), 
                int(row[4]), 
                int(row[5]))
                lista_de_tareas.append((holder, float(row[6])))
    print("Info loaded")
 #   if len(content)==0:        print("no content")        return
    

def tarea_saver():
    with open(file_path, "w", newline="") as file:
        print("Started saving")
        writer = csv.writer(file)
        for tarea in lista_de_tareas:
            objeto = tarea[0]
            valor = tarea[1]
            writer.writerow([objeto.name, objeto.priority, objeto.complexity, objeto.day, objeto.month, objeto.year,valor])

lista_de_tareas = []

def print_date():
    print(cal.selection_get())

def tarea_setter():
    nombre = entrada.get().strip()

    if not nombre:
        messagebox.showwarning("Error", "Escribe un nombre")
        return 
    
    nombre_de_tarea = nombre
    nombre_de_tarea = Tareas.Tareas(
        nombre, 
        priority.get(), 
        complexity.get(), 
        cal.selection_get().day, 
        cal.selection_get().month, 
        cal.selection_get().year
        )
    print("Priority:", nombre_de_tarea.priority)
    print("Complexity:", nombre_de_tarea.complexity)
    print("Due date:", nombre_de_tarea.due_date)
    lista_de_tareas.append((nombre_de_tarea, nombre_de_tarea.complexity*nombre_de_tarea.priority*1000000/(nombre_de_tarea.due_date-(hoy.day+hoy.month*100+hoy.year*10000)+0.1) ))
    lista_de_tareas.sort(key=lambda x: x[1], reverse=True)
    lista.insert(tk.END, nombre)
    entrada.delete(0, tk.END)
    actualizar_lista()
    for tarea in lista_de_tareas:
        print(tarea[0].name, tarea[1])

def actualizar_lista():
    lista.delete(0, tk.END)

    for tarea in lista_de_tareas:
        lista.insert(tk.END, f"{tarea[0].name} - {tarea[1]:.2f}")

def agregar_texto(event=None):
    nombre = entrada.get().strip()
    if nombre:
        lista.insert(tk.END, nombre)
        entrada.delete(0, tk.END)

root = tk.Tk()
root.title('TaskNot3')

marco_entrada = tk.Frame(root)
marco_entrada.pack(fill="x", padx=10, pady=10)

marco_selectores = tk.Frame(root)
marco_selectores.pack(fill="x", padx=10)

priority = tk.Scale(
    marco_selectores,
    from_=1,
    to=5,
    orient=tk.HORIZONTAL,
    resolution=1,
    label="priority"
)
priority.pack(fill="x")

complexity = tk.Scale(
    marco_selectores,
    from_=1,
    to=5,
    orient=tk.HORIZONTAL,
    resolution=1,
    label="complexity"
)
complexity.pack(fill="x")

entrada = tk.Entry(marco_entrada)
entrada.pack(side="left", fill="x", expand=True)
entrada.bind("<Return>", agregar_texto)

tk.Button(marco_entrada, text="Agregar", command=tarea_setter).pack(side="right", padx=(8, 0))

marco_contenido = tk.Frame(root)
marco_contenido.pack(fill="both", expand=True)

marco_calendario = tk.Frame(marco_contenido)
marco_calendario.pack(side="left", fill="y")

lista = tk.Listbox(marco_contenido, width=30, height=12)
lista.pack(side="right", fill="both", expand=True, padx=10, pady=10)

cal = Calendar(root, selectmode = 'day', year = hoy.year, month = hoy.month, day= hoy.day)
cal.pack(pady=20)

tk.Button(root, text='Salvar', command=tarea_saver).pack(pady=20)

onetimereader()
root.mainloop()