import enum


#################ENUMS###############################################

class ACCESSLEVEL(enum.Enum):
    ROOT = 0
    ADMIN = 1
    PUBLIC_USER = 2

class DAY(enum.Enum):
    TTh = 0
    MW = 1
    MWF = 2
    TThF = 3
    MF = 4
    WF = 5
    TF = 6
    ThF = 7
    M = 8
    T = 9
    W = 10
    Th = 11
    F = 12

class DISCIPLINES(enum.Enum):
    ProgrammingC = 0
    ProgrammingPython = 1
    GameDevelopment = 2
    DataStructuresandAlgorithms = 3
    ComputerOrganization = 4
    OperatingSystems = 5
    ProgrammingLanguages = 6
    Cybersecurity = 7
    MobileApplications = 8
    ArtificialIntelligence = 9
    Networks = 10
    TheoryOfComputation = 11
    ParallelandDistributedSystems = 12
    VirtualReality = 13


#################TUPLES###############################################


RegistrationRequest = (
    str,         #proposedUserName,
    str,         #proposedPassword,
    str,         #emailAddress,
    ACCESSLEVEL
)

UserAccountInfo = (
    str,         #userName,
    str,         #Password,
    str,         #emailAddress,
    ACCESSLEVEL
)

Course = (
    int,          #sectionNum,
    str,          #departmentCode("CPSC"),
    DAY,
    int,          #length,
    int,          #startTime,
    set           #Subjects = [ set of DISCIPLINES ]
)

Instructor = (
    str,          #firstName,
    str,          #lastName,
    str,          #email,
    set,          #Expertise = ((set of DISCIPLINES)),
    set,          #courses = ((set of ref(course))),
    int,          #maxLoad,
    list          #schedule = [List of Dictionaries]
)

OutputSchedule = (
    set,          #courses = ((set of ref(courses)))
    bool,         #isValid,
    bool,         #facultyOverLoad,
    bool          #notEnoughFaculty
)


#################SETS###############################################


AllCourses = (( ))

Instructors = (( ))


#################QUEUES###############################################


unnassignedCourseQueue = [ ]

registrationRequestQueue = [ ]


#################LISTS###############################################


outputSchedules = [ ]

validUsers = [ ]

schedule = [{   #list of dictionarys call syntax is schedule[2][2200] that will call Tuesday at 10pm
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
},{     # Monday^
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
},{     # Tusday^
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
},{    # Wednesday^
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
},{     # Thursday^
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
}]   # Friday^

#print(schedule[2][2200])
