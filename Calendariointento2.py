import tkinter as tk
from tkcalendar import Calendar
from datetime import date
import Tareas
import os
from tkinter import messagebox

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "saver.csv")



def onetimereader():
    try:
        with open(file_path, "x") as file:
            print("file created")
    except FileExistsError:
        print("file exists")

    with open(file_path, "r") as file:
        content = file.read()
    print("Info loaded")
    for row in content:
        holder=Tareas.Tareas(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))
        lista_de_tareas.append((holder, int(row[6])))

hoy = date.today()

print(hoy)

lista_de_tareas = []

def print_date():
    print(cal.selection_get())

def tarea_setter(name, priority, complexity):
    name = Tareas.Tareas(
        name, 
        priority, 
        complexity, 
        cal.selection_get().day, 
        cal.selection_get().month, 
        cal.selection_get().year
        )
    lista_de_tareas.append(("Prueba", name.complexity*name.priority*10/((hoy.day+hoy.month*100+hoy.year+10000)-name.due_date+0.1) ))
    lista_de_tareas.sort(key=lambda x: x[1])
    print(lista_de_tareas)

def agregar_texto(event=None):
    texto = entrada.get().strip()
    if texto:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)


root = tk.Tk()
root.title('TaskNot3')

marco_entrada = tk.Frame(root)
marco_entrada.pack(fill="x", padx=10, pady=10)

entrada = tk.Entry(marco_entrada)
entrada.pack(side="left", fill="x", expand=True)
entrada.bind("<Return>", agregar_texto)

tk.Button(marco_entrada, text="Agregar", command=agregar_texto).pack(side="right", padx=(8, 0))

marco_contenido = tk.Frame(root)
marco_contenido.pack(fill="both", expand=True)

marco_calendario = tk.Frame(marco_contenido)
marco_calendario.pack(side="left", fill="y")

lista = tk.Listbox(marco_contenido, width=30, height=12)
lista.pack(side="right", fill="both", expand=True, padx=10, pady=10)

root = tk.Tk()
root.title('Calendario interactivo')

cal = Calendar(root, selectmode = 'day', year = hoy.year, month = hoy.month, day= hoy.day)
cal.pack(pady=20)

entrada = tk.Entry(root)
entrada.pack(pady=10)

texto = entrada.get()

tk.Button(root, text='Seleccionar Fecha', command=tarea_setter).pack(pady=20)

root.mainloop()