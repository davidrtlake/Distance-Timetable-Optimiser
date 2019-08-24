import math

coordinates = {"1":(766,598), "2":(898,560),"3":(899,642),"3A":(377,377),
               "4":(884,698),"5":(839,718),"6":(812,774),"7":(779,752),
               "8":(688,709),"9":(644,642),"11":(662,552),"12":(828,498),
               "12A":(851,532),"14":(823,457),"17":(860,742),"20":(922,676),
               "21A":(982,637),"21B":(1023,653),"21C":(1057,646),
               "21D":(1024,604),"22":(1058,592),"23":(967,557),"24":(943,508),
               "24A":(949,456),"25":(1016,488),"26":(1017,414),"26A":(1036,437),
               "26B":(1026,390),"27":(1095,382),"27A":(1081,495),"28":(989,323),
               "28B":(1008,326),"29":(968,318),"29A":(680,213),"30":(738,35),
               "31A":(980,474),"31B":(992,450),"32":(1004,538),"33":(1094,576),
               "35":(917,416),"37":(924,370),"38":(976,500),"39":(858,360),
               "39A":(820,363),"40":(679,172),"41":(917,789),"42":(826,816),
               "43":(810,857),"44":(856,842),"45":(866,886),"47":(894,952),
               "47A":(874,952),"49":(974,886),"50":(792,931),"51":(922,833),
               "51A":(977,828),"57":(676,976),"60":(681,949),"61":(609,768),
               "61A":(589,779),"62":(673,806),"63":(662,831),"64":(687,871),
               "64A":(680,907),"65":(824,840),"67":(759,829),"68":(747,893),
               "69":(723,830),"72":(630,922),"73":(704,1073),"74":(836,995),
               "75":(726,1027),"76":(737,949),"78":(972,944),"79":(638,886),
               "80":(458,721),"80A":(485,703),"80B":(373,725),"81":(519,667),
               "82A":(529,587),"82B":(531,562),"82C":(537,535),"82D":(501,530),
               "82E":(475,550),"82F":(503,558),"82G":(501,569),"82J":(540,549),
               "82K":(534,572),"82L":(473,590),"82M":(495,596),"83":(531,494),
               "84":(489,630),"84A":(492,659),"85":(441,664),"86":(432,600),
               "87":(440,523),"87A":(427,575),"88":(430,417),"89C":(312,445),
               "89E":(471,427),"89F":(400,394),"90":(320,575),"91":(267,594),
               "91C":(286,569),"91D":(301,577),"92A":(140,460),"93C":(394,785),
               "93D":(504,289),"94":(594,594),"96":(321,604),"97":(444,566),
               "98A":(510,380),"98B":(440,364),"99":(306,360)}

buildingA = input("Building A: ")
buildingB = input("Building B: ")

def distance(bA, bB):
    """return the distance between two buildings"""
    ds = -1

    try:
        for key in coordinates.keys():
            A = coordinates.get(bA)
            B = coordinates.get(bB)
            ##math.fabs(x) Return the absolute value of x.
            ds = round(pow(pow(math.fabs(A[0]-B[0]),2)+pow(math.fabs(A[1]-B[1]),2),1/2))

    except TypeError as e:
        print("Wrong building number")
    else:
        print("coordA =",A)
        print("coordB =",B)
        print("The distance is",ds)
        
    return ds

distance(buildingA, buildingB)

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

    def GetBuildings(self, day):
        buildings = []
        for i in range(0, len(self.days)):
            if self.days[i] == day:
                buildings.append(self.buildings[i])
        print(buildings)
        
    def GetSessions(self, day):
        sessions = []
        for i in range(0, len(self.times)):
            if self.days[i] == day:
                sessions.append(self.times[i])
        print(sessions)

    
#Making classes
CSSE2310Practical = Class([[10, 11], [8, 10], [8, 10], [10, 12], [12, 14],
                           [14, 16], [16, 18], [14, 16], [18, 20], [16, 18],
                           [18, 20]], [3, 3, 2, 1, 1, 1, 1, 2, 2, 4, 4],
                          ["50", "50", "50", "50", "50", "50",
                           "50", "50", "50", "50", "50"], True, True)
CSSE2310Lecture = Class([[12, 13], [15]], [3, 4], ["27A", "49"], True, True)
COMP3506Tute = Class([14, 15, 16, 17, 8, 9, 12, 13, 9, 10, 11, 11, 11],
                     [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 5],
                     ["01", "01", "09", "35", "83", "83", "09", "09",
                      "83", "09", "09", "09", "35"], False, False)
COMP3506Lecture = Class([[8, 9, 10]], [4], ["27A"], True, True)
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
CSSE2310Practical.GetBuildings(1)
CSSE2310Practical.GetSessions(1)

    
