import array as arr

class Tareas:
    def __init__(self, name, priority, complexity, day, month, year):
        self.name = name
        self.priority = priority
        self.complexity =  complexity
        self.due_date = day+month*100+year+10000
