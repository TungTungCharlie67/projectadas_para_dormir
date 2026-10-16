import tkinter as tk
from tkcalendar import Calendar
from datetime import date
import Tareas

hoy = date.today()

print(hoy)

lista_de_tareas = []


def print_date():
    print(cal.selection_get())

def tarea_setter():
    Prueba = Tareas.Tareas(
        "Prueba", 
        1, 
        1, 
        cal.selection_get().day, 
        cal.selection_get().month, 
        cal.selection_get().year
        )
    lista_de_tareas.append(("Prueba", Prueba.complexity*Prueba.priority*10/((hoy.day+hoy.month*100+hoy.year+10000)-Prueba.due_date) ))
    lista_de_tareas.sort(key=lambda x: x[1])
    print(lista_de_tareas)


root = tk.Tk()
root.title('Calendario interactivo')

cal = Calendar(root, selectmode = 'day', year = hoy.year, month = hoy.month, day= hoy.day)
cal.pack(pady=20)

tk.Button(root, text='Seleccionar Fecha', command=tarea_setter).pack(pady=20)

root.mainloop()