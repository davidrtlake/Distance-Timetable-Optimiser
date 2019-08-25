coordinates = {"30":(736,31), }

class Timetable():
    courses = []
    def __init__(self, courses):
        self.courses = courses

    def CreateTimetable(self):
        pass

    """
        Iterates through days and classes to remove conflicts.
        Currently throws an error when using .remove
    """
    def RemoveConflicts(self):
        #print(self.courses.classes.times)
        """for i in range(0, 5):       
            if item in nonStaticClasses[i]:
                for course in self.courses:
                    for classs in course.classes:
                        for time in classs.times:
                            for day in classs.days:
                                if day == i and time == item:
                                    print(i)
                                    print(item)
                                    classs.days.remove(i)
                                    classs.times.remove(item)
                                    print(classs.days)"""
        pass
        #print(self.courses.classes.times)
                            

class Course():
    name = ""
    classes = []
    global staticClasses
    global nonStaticClasses
    staticClasses = ([],[],[],[],[])
    nonStaticClasses = ([],[],[],[],[])
    def __init__(self, name, classes):
        self.classes = classes
        self.name = name

    def PrintCourse(self):
        print("The course name is " + self.name + " and the class times are")
        for classs in self.classes:
            for times in classs.days:
                print(" " + str(times) + " ")

    """
        Iterates through each class and each session and appends the session
        to the appropriate array in the staticClasses list if the class is static
        and compulsory.
    """
    def GetStatic(self):
        for classs in self.classes:
            if classs.static == True and classs.compulsory == True:
                for i in range(0, len(classs.times)):
                    staticClasses[(classs.days[i]-1)].append(classs.times[i])
        return staticClasses

    """
        Iterates through each class and each session and appends the session
        to the appropriate array in the nonStaticClasses list if the class is
        non static but compulsory.
    """
    def GetNonStatic(self):
        for classs in self.classes:
            if classs.static == False and classs.compulsory == True:
                for i in range(0, len(classs.times)):
                    nonStaticClasses[(classs.days[i]-1)].append(classs.times[i])
        return nonStaticClasses
        

class Class:
    times = []
    days = []
    buidlings = []
    static = False
    compulsory = False
    def __init__(self, times, days, buildings, static, compulsory):
        self.times = times
        self.days = days
        self.buildings = buildings
        self.static = static
        self.compulsory = compulsory

    
#Making classes
CSSE2310Practical = Class([10, 11], [3, 3], ["50"], True, True)
CSSE2310Lecture = Class([12, 13, 15], [3, 3, 4], ["27A", "49"], True, True)
COMP3506Tute = Class([14, 15, 16, 17, 8, 9, 12, 13, 9, 10, 11, 11, 11],
                     [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 5],
                     ["01", "01", "09", "35", "83", "83", "09", "09",
                      "83", "09", "09", "09", "35"], False, True)
COMP3506Lecture = Class([8, 9, 10], [4, 4, 4], ["27A"], True, True)
#Making courses
CSSE2310 = Course("CSSE2310", [CSSE2310Practical, CSSE2310Lecture])
COMP3506 = Course("COMP3506", [COMP3506Tute, COMP3506Lecture])
#Creates timetable of courses
Timetable = Timetable([CSSE2310, COMP3506])
"""
    For each courses in the timetable, produce a 2d list of arrays of static
    and non static class times.
"""
for course in Timetable.courses:
    course.GetStatic()
    course.GetNonStatic()
print("STATIC", staticClasses)
print("NON STATIC", nonStaticClasses)
Timetable.RemoveConflicts()
