import tkinter as tk
from tkcalendar import Calendar
from datetime import date
import Tareas
import os

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


root = tk.Tk()
root.title('Calendario interactivo')

cal = Calendar(root, selectmode = 'day', year = hoy.year, month = hoy.month, day= hoy.day)
cal.pack(pady=20)

tk.Button(root, text='Seleccionar Fecha', command=tarea_setter).pack(pady=20)

root.mainloop()