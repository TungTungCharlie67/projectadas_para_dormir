import array as arr
name
priority
due_date 
complexity

class Tareas:
    def __init__(name, priority, complexity, day, month, year):
        self.name = name
        self.priority = priority
        self.complexity =  complexity
        self.due_date = day+month*100+year+10000
