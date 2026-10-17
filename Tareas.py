class Tareas:
    def __init__(self, name, priority, complexity, day, month, year):
        self.name = name
        self.priority = priority
        self.complexity =  complexity
        self.day= day
        self.month = month
        self.year = year
        self.due_date = day+month*100+year*10000
