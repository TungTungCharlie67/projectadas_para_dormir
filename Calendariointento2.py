import tkinter as tk
import tkcalendar 
from datetime import date
import Tareas
import os
import csv
from tkinter import messagebox
from datetime import date

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
                row[3])
                lista_de_tareas.append((holder, float(row[4])))
    print("Info loaded")
    

def tarea_saver():
    with open(file_path, "w", newline="") as file:
        print("Started saving")
        writer = csv.writer(file)
        for tarea in lista_de_tareas:
            objeto = tarea[0]
            valor = tarea[1]
            writer.writerow([objeto.name, objeto.priority, objeto.complexity, objeto.due_date, valor])

lista_de_tareas = []


def tarea_setter(nombre, priority, complexity, due_date):
    nombre = entrada.get().strip()

    if not nombre:
        messagebox.showwarning("Error", "Escribe un nombre")
        return 
    
    nombre_de_tarea = Tareas.Tareas(
        nombre, 
        priority, 
        complexity, 
        due_date
        )
    lista_de_tareas.append((nombre_de_tarea, prioratizer(priority, complexity, due_date)))
    lista_de_tareas.sort(key=lambda x: x[1], reverse=True)
    lista.insert(tk.END, nombre)
    entrada.delete(0, tk.END)
    actualizar_lista()


def eliminar_tarea():
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showwarning("Error67", "Selecciona una tarea para eliminar")
        return


    del lista_de_tareas[seleccion[0]]
    actualizar_lista()
    tarea_saver()


def prioratizer(priority, complexity, due_date):
    if isinstance(due_date, str):
        due_date = datetime.strptime(due_date, "%m/%d/%y").date()

    remaining_dates = (due_date - hoy).days

    if remaining_dates < 0:
        remaining_dates = -10000

    return priority*40 + complexity*20 - remaining_dates

def actualizar_lista():
    lista.delete(0, tk.END)

    for tarea in lista_de_tareas:
        lista.insert(tk.END, f"{tarea[0].name} - {tarea[1]:.2f}")

def agregar_texto(event=None):
    tarea_setter(entrada.get().strip(), priority.get(), complexity.get(), cal.selection_get())

def Checador_para_el_dia(List):
    for tarea in List:
            if date.today().isoformat() == tarea[0].due_date:
                messagebox.showwarning("Holder i guess", f"{tarea[0].name} se entrega hoy")

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

cal = tkcalendar.Calendar(root, selectmode = 'day', year = hoy.year, month = hoy.month, day= hoy.day)

entrada = tk.Entry(marco_entrada)
entrada.pack(side="left", fill="x", expand=True)
entrada.bind("<Return>", lambda event: tarea_setter(entrada.get().strip(), priority.get(), complexity.get(), cal.selection_get()))

tk.Button(marco_entrada, text="Agregar", command=lambda: tarea_setter(entrada.get().strip(), priority.get(), complexity.get(), cal.selection_get())).pack(side="right", padx=(8, 0))

marco_contenido = tk.Frame(root)
marco_contenido.pack(fill="both", expand=True)

marco_calendario = tk.Frame(marco_contenido)
marco_calendario.pack(side="left", fill="y")

lista = tk.Listbox(marco_contenido, width=30, height=12)
lista.pack(side="right", fill="both", expand=True, padx=10, pady=10)
tk.Button(marco_contenido, text="Eliminar tarea", command=eliminar_tarea).pack(side="right", padx=5)


cal.pack(pady=20)

tk.Button(root, text='Salvar', command=tarea_saver).pack(pady=20)

onetimereader()
actualizar_lista()
Checador_para_el_dia(lista_de_tareas)
root.mainloop()