import random
import requests
import json

CONNECTION_STRING = "http://localhost:5000"


def input_float(request):
    num = ""
    while not num.isdigit():
        num = input(request)

    return float(num) 

def input_int(request):
    return int(input_float(request))

class CourseMarks:

    def __init__(self, course_id):
        self.course_id = course_id
        self.input_functions = [self.input_lat, self.input_lon, self.input_descrip, self.input_isStart, self.input_rounding, self.input_gate]
        self.create_new()
        
        self.id = random.randint(0, 999999999999)
        
        print("this mark has been created and has id: " + str(self.id))

    # TODO
    def json_create(self):
        return {'lat': self.lat, 'lon': self.lon, 'description': self.descrip, 'rounding': self.rounding, 'isStart': self.isStart ,'gate':self.gate}

    def input_lat(self):
        self.lat = input_float("Input Latitude: ")

    def input_lon(self):
        self.lon = input_float("Input longitude: ")
 
    def input_descrip(self):
        self.descrip = input("Input description: ")
 
    def input_rounding(self):
        self.rounding = None
        if( not self.isStart):
            responce = input("Is this a rounding? Y/N \n")
            
            if (responce == "y" or responce == "Y"):
                responce = input("port or starboard? P/S \n")
                if(responce == "p" or responce == "P"):
                    self.rounding = False 
                if(responce == "s" or responce == "S"):
                    self.rounding = True
 
    def input_isStart(self):
        self.isStart = None
        responce = input("is this mark a part of the start or finsish S/F input anything else if none \n")
        if(responce == "f" or responce == "F"):
            self.isStart = False 
        if(responce == "s" or responce == "S"):
            self.isStart = True
 
    def input_gate(self):
        self.gate = None
        responce = input("is this mark a part of a gate? Y/N Only input if this is the second mark created that is a gate \n")
        if (responce == "y" or responce == "Y"):
            self.gate =  int(input("give the integer id of the mark that this creates a gate with \n"))
 
    def create_new(self):
        for function in self.input_functions:
            function()



class Course:

    def __init__(self):
        self.input_functions = [self.input_name, self.input_description, self.input_marks]
        self.id = random.randint(0, 999999999999)
        self.create_new()

        self.id = requests.post(CONNECTION_STRING + "/Course", self.json_create())
        print(self.id.json())

        print("this course has been created and has id: " + str(self.id))

    # TODO
    def json_create(self):
        marks = []
        for mark in self.marks:
            marks.append(mark.json_create())
        return {'name': self.name, 'description': self.description, 'marks': marks}
        

    def create_new(self):
        for function in self.input_functions:
            function()

    def input_name(self):
        self.name = input("Input course name: ")
 
    def input_description(self):
        self.description = input("Input Description: ")
 
    def input_marks(self):
        num_marks = input_int("How many marks would you like to create?\n")

        self.marks = list()
        for i in range(num_marks):
            self.marks.append(CourseMarks(self.id))
        
class Race:

    def __init__(self):
        self.input_functions = []
        self.create_new()
        
        self.id = requests.post(CONNECTION_STRING + "/race", self.json_create()) 
        
        print("this race has been created and has id: " + str(self.id))

    def get():
        responce = input("get specific race? Y/N \n")

        if (responce == "y" or responce == "Y"):
            id = input_int("Input race Id: ") 
            print( requests.get(CONNECTION_STRING + "/race" + str(id)).json())
        else:
            print( requests.get(CONNECTION_STRING + "/race").json())

    def get_results():
        id = input_int("Input race Id: ") 
        print(requests.get(CONNECTION_STRING + "/race/" + str(id) + "/results").json())

    def create_new(self):
        for function in self.input_functions:
            function()


    # TODO
    def json_create(self):
        print("TODO")

    def input_Name(self):
        self.name = input("Input name: ")

    def input_start_time(self):
        self.start_time = input("Input start time: ")

    def input_end_time(self):
        self.end_time = input("Input end time: ")

    def input_course_id(self):

        responce = input("Is there a course already created that you would like to use for this race? Y/N \n")

        if (responce == "y" or responce == "Y"):
            self.course_id = input_int("Input Course Id: ")
        else:
            self.course_id = Course()

    def input_regatta_id(self):
        self.regatta_id = None
        responce = input("Would you like to attach this race to a regatta Y/N \n")

        if (responce == "y" or responce == "Y"):
            self.course_id = input_int("Input Regatta Id: ")

USER_ACTIONS = [Race, Course, Race.get, Race.get_results]
USER_OPTIONS = ["Create a race", "Create a course", "Get race data", "Get race results"]

while True:
    print("actions avalible: ")
    for i in range(len(USER_OPTIONS)):
        print(str(i) + ": " + USER_OPTIONS[i])    

    option = input("Give requested option 1,2,... \n")
    if option.isdigit():
        option = int(option)

        if option > 0 and option < len(USER_ACTIONS):
            USER_ACTIONS[option]()

    