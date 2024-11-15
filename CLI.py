import random


class CourseMarks:

    def __init__(self):
        self.id = random.randint()
        self.lat
        self.lon
        self.descrip 
        self.rounding
        self.isStart 
        self.gate 
        
        self.input_functions = [self.input_lat, self.input_lon, self.input_descrip, self.input_rounding, self.input_isStart, self.input_gate]

        self.createNew(self)
        print("this mark has been created and has id: " + id)

    def input_lat(self):
        self.lat = input("Input Latitude:")

    def input_lon(self):
        self.lon = input("Input :")
 
    def input_descrip(self):
        self.descrip = input("Input :")
 
    def input_rounding(self):
        self.rounding = input("Input :")
 
    def input_isStart(self):
        self.isStart = input("Input :")
 
    def input_gate(self):
        self.gate = input("Input :")
 
    def createNew(self):
        for function in self.input_functions:
            function(self)



class Course:
    input_functions = []

    def __init__(self):
        self.id = random.randint() 
        self.createNew(self)
        print("this course has been created and has id: " + id)

    def __init__(self, id, name, description, marks):
        self.id = random.randint() 
        self.name = name
        self.description = description
        self.marks = marks
        print("this course has been created and has id: " + id)

    def createNew(self):
        for function in self.input_functions:
            function(self)

    def input_name(self):
        self.name = input("Input :")
 
    def input_description(self):
        self.description = input("Input :")
 
    def input_marks(self):
        num_marks = int(input("How many marks would you like to create?"))

        for i in num_marks:
            self.marks.append(CourseMarks())
        
 



