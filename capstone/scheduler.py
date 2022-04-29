from capstone import db
from capstone.models import sections, instructors, output_schedule
import enum
import random
MaxLoadedInstructors = []
outputSchedules = [ ]
instructorQueue = []
AllCourses = []

#################ENUMS###############################################

class ACCESSLEVEL(enum.Enum):
    ROOT = 0
    ADMIN = 1
    PUBLIC_USER = 2

class DAY(enum.Enum):
    TR = 0
    MW = 1
    MWF = 2
    TRF = 3
    MF = 4
    WF = 5
    TF = 6
    RF = 7
    M = 8
    T = 9
    W = 10
    R = 11
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


#################LISTS###############################################

schedule = [{   #list of dictionarys call syntax is schedule[2][2200] that will call Tuesday at 10pm
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
}]   # Friday^

Schedule = [{   #list of dictionarys call syntax is schedule[2][2200] that will call Tuesday at 10pm
   800 : 0,   830 : 0,
   900 : 0,   930 : 0,
  1000 : 0,  1030 : 0,
  1100 : 0,  1130 : 0,
  1200 : 0,  1230 : 0,
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
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
  1300 : 0,  1330 : 0,
  1400 : 0,  1430 : 0,
  1500 : 0,  1530 : 0,
  1600 : 0,  1630 : 0,
  1700 : 0,  1730 : 0,
  1800 : 0,  1830 : 0,
  1900 : 0,  1930 : 0,
  2000 : 0,  2030 : 0,
  2100 : 0,  2130 : 0,
  2200 : 0,  2230 : 0,
}]   # Friday^


#  0 or 1 for prof or course accordingly, number of records being imported, path to file  #
def importData(prof_or_course, record_num, file_path):

  data = open(file_path)
  data_string = data.read()
  data.close()

  for i in range(record_num):
    # split the file dynamically
    one_go = [name.strip() for name in data_string.split(':')[i].split(',')]
    #print("Data imported as: {}".format(one_go))


    # add data to course queue
    if prof_or_course == 1:
      code = int(one_go[0])       #0
      dep_num = one_go[1]         #1
      day = one_go[2]             #2
      length = int(one_go[3])     #3
      time = int(one_go[4])       #4
      disc = one_go[6]            #5
      periods = 0                 #6
      name = one_go[5]            #7
      Course_temp = (code,dep_num,day,length,time,disc,periods,name)
      AllCourses.append(Course_temp)

      section = sections(Code=code, DepartmentCode=dep_num, Day=day, Length=length, StartTime=time, Disciplines=disc, Periods=periods, Name=name, instructor=None)
      db.session.add(section)
      db.session.commit
    # add data to instructor queue
    elif prof_or_course == 0:
      lname = one_go[0]                 #0
      maxload = int(one_go[1])          #1
      disc = one_go[2]                  #2
      courses = []                      #3
      inst_schedule = list(schedule)    #4
      currload = 0                      #5
      prof_temp = (lname,maxload,disc,courses,schedule,currload)
      instructorQueue.append(prof_temp)

    else:
      print("incorrect data value: Error Code 101")

      prof = instructors(LName=lname, MaxLoad=maxload, Disciplines=disc, Course_code_1=None, Course_code_2=None, Course_code_3=None, Course_code_4=None, Schedule_Day_1=None, Schedule_Day_2=None, Schedule_Day_3=None, Schedule_Day_4=None, Schedule_Day_5=None, CurrentLoad=currload)
      db.session.add(prof)
      db.session.commit


#############      storage conversions     #####################################
def convertScheduleToStrings(schedule):

  dayStrings = []
  for i in range(5):
    string = ""
    timeHolder = 730

    for j in range(30):
      difference = 30
      if timeHolder % 100 != 0:
        difference = 70
      timeHolder = timeHolder + difference
      temp = str(schedule[i][timeHolder])
      string = string + temp
    dayStrings.append(string)
  return dayStrings

def convertStringsToSchedule(strings):

  tempSchedule = schedule
  for i in range(5):
    timeHolder = 730

    for j in range(30):
      difference = 30
      if timeHolder % 100 != 0:
        difference = 70
      timeHolder = timeHolder + difference
      tempSchedule[i][timeHolder] = strings[i][j]
  return tempSchedule

#################   HELPER FUNCTIONS    ########################################
def getRandomNum(lowerBound, upperBound):
  rand = random.randint(lowerBound,upperBound) - 1
  return rand

#####         Alter tuple Value         #####
def changeTupleValue(selectedTuple,newValue,changePos):
  left = selectedTuple[0:changePos]
  right = selectedTuple[(changePos+1):]
  selectedTuple = left + (newValue,) + right
  return selectedTuple

#####           Set the amount of periods in a section          #####
def setPeriods(course):
  if course[3] == 50:
    course = changeTupleValue(course,2,6)
  elif course[3] == 75:
    course = changeTupleValue(course,3,6)
  elif course[3] == 150:
    course = changeTupleValue(course,5,6)
  else:
    print("Course Length value incorrect. Length is,", course[3], "ERROR: Code 102.")
  return course

#####     check instructor schedule    #####
def CheckInstSched(instructor, course):

  for i in range(course[6]):
    #establish next period interval
    timeholder = course[4]
    difference = 30
    if timeholder % 100 != 0:
      difference = 70
    if i != 0:
      timeholder = course[4] + difference

    #Monday
    if course[2] == "MWF" or course[2] == "MW" or course[2] == "MF" or course[2] == "M":      #if monday
      if (instructor[4][0][timeholder]) == 1:                                                 #check time slot
        return False                                                                          #return false if slot is filled
    #Tuesday
    if course[2] == "T" or course[2] == "TR" or course[2] == "TF" or course[2] == 'TRF':      #Rinse repeat for each day
      if (instructor[4][1][timeholder]) == 1:
        return False
    #Wednesday
    if course[2] == "W" or course[2] == "WF" or course[2] == "MWF" or course[2] == "MW":
      if (instructor[4][2][timeholder]) == 1:
        return False
    #Thursday
    if course[2] == "R" or course[2] == "RF" or course[2] == "TR" or course[2] == "TRF":
      if (instructor[4][3][timeholder]) == 1:
        return False
    #Friday
    if course[2] == "F" or course[2] == "RF" or course[2] == "TRF" or course[2] == "MF" or course[2] == "MWF" or course[2] == "WF" or course[2] == "TF":
      if (instructor[4][4][timeholder]) == 1:
        return False
  return True                                                                   #return true if all slots checked are empty

#####     add course to instructor schedule    #####
def schedInstSched(instructor, course):   #0 = sched | 1 = overlap
  # assign class to lowest of 3 empty spots in instructor list
  instructor[3].append(course)

  # set the value for each of the class periods to 1 from 0 in each day
  for i in range(course[6]):

    timeholder = course[4]                                                      #establish whether next period interval will be 30 or 70
    difference = 30
    if timeholder % 100 != 0:
      difference = 70
    if i != 0:
      timeholder = course[4] + difference

    #Monday
    if course[2] == "MWF" or course[2] == "MW" or course[2] == "MF" or course[2] == "M":      #if monday
      instructor[4][0][timeholder] = 1                                                        #set timeslot positive
    #Tuesday
    if course[2] == "T" or course[2] == "TR" or course[2] == "TF" or course[2] == "TRF":      # rinse repeat for each day
      instructor[4][1][timeholder] = 1
    #Wednesday
    if course[2] == "W" or course[2] == "WF" or course[2] == "MWF" or course[2] == "MW":
      instructor[4][2][timeholder] = 1
    #Thursday
    if course[2] == "R" or course[2] == "RF" or course[2] == "TR" or course[2] == "TRF":
      instructor[4][3][timeholder] = 1
    #Friday
    if course[2] == "F" or course[2] == "RF" or course[2] == "TRF" or course[2] == "MF" or course[2] == "MWF" or course[2] == "WF" or course[2] == "TF":
      instructor[4][4][timeholder] = 1
  return instructor

#####           Find match rate between instructor and section          ######
def findMatchRate(disciplines,subjects):
  #split disciplines to individual strings
  disciplines_split = [name.strip() for name in disciplines.split('.')]

  #split subjects to individual strings
  subjects_split = [name.strip() for name in subjects.split('.')]

  match_rate = 0
  for i, str in enumerate(disciplines_split):
    for j, str in enumerate(subjects_split):
      if disciplines_split[i] == subjects_split[j]:
        match_rate = match_rate + 1
  #print(disciplines_split[i],"|",subjects_split[j],"=",match_rate)
  return(match_rate)

#####         find the amount of overlap between old instructor courses and course          ######
def findMinOverlap(instructor,course):

  for i in range(course[6]):
    overlap = 0

    timeholder = course[4]                                                      #establish whether next period interval will be 30 or 70
    difference = 30
    if timeholder % 100 != 0:
      difference = 70
    if i != 0:
      timeholder = course[4] + difference


    #Monday
    if course[2] == "MWF" or course[2] == "MW" or course[2] == "MF" or course[2] == "M":    #if monday
      if (instructor[4][0][timeholder]) == 1:                                               #check timeslot
        overlap = overlap + 1                                                               #increase period overlap amount
    #Tuesday
    if course[2] == "T" or course[2] == "TR" or course[2] == "TF" or course[2] == 'TRF':    # rinse repeat for each day
      if (instructor[4][1][timeholder]) == 1:
        overlap = overlap + 1
    #Wednesday
    if course[2] == "W" or course[2] == "WF" or course[2] == "MWF" or course[2] == "MW":
      if (instructor[4][2][timeholder]) == 1:
        overlap = overlap + 1
    #Thursday
    if course[2] == "R" or course[2] == "RF" or course[2] == "TR" or course[2] == "TRF":
      if (instructor[4][3][timeholder]) == 1:
        overlap = overlap + 1
    #Friday
    if course[2] == "F" or course[2] == "RF" or course[2] == "TRF" or course[2] == "MF" or course[2] == "MWF" or course[2] == "WF" or course[2] == "TF":
      if (instructor[4][4][timeholder]) == 1:
        overlap = overlap + 1
  return overlap

#####           Assign course a instructors full schedule         #####
def reassignCourse(instructor,course,courseQueue,courseIndice):
  #make list matching the instructors course list
  #empty his course list
  #empty his schedule
  #assign new course
  #assign old courses
  #add the remaining course back to unassigned courses

  if instructor[5] == 2:
    print("instructors course list before:", instructor[3][0][7],"|",instructor[3][1][7])
  elif instructor[5] == 3:
    print("instructors course list before:", instructor[3][0][7],"|",instructor[3][1][7],"|",instructor[3][2][7])
  elif instructor[5] == 4:
    print("instructors course list before:", instructor[3][0][7],"|",instructor[3][1][7],"|",instructor[3][2][7],"|",instructor[3][3][7])


  new_instructor = None
  instCourses = list(instructor[3])                                             #copy course list
  instructor[3].clear()                                                         #empty course list
  new_instructor = changeTupleValue(instructor,Schedule,4)                      #empty schedule
  new_instructor = schedInstSched(new_instructor,course)                        #assign new course
  #print("schedule:       ",instructor[4])
  indice = 0
  loopNum = len(instCourses)
  for i in range(loopNum):
    if CheckInstSched(new_instructor,instCourses[indice]) and i < instructor[1]:
      #print("#",i,"| sched     ",instructor[4])
      new_instructor = schedInstSched(new_instructor,instCourses[indice])
      del instCourses[indice]
      #remove course i from instCourses
    else:
      #print("in else | sched",instructor[4])
      indice = indice + 1


  newCurrLoad = len(new_instructor[3])
  new_instructor = changeTupleValue(new_instructor,newCurrLoad,5)

  del courseQueue[courseIndice]
  #remove inst from old course
  if new_instructor != None:
    if new_instructor[5] == 2:
      print("instructors course list after:", new_instructor[3][0][7],"|",new_instructor[3][1][7])
    elif new_instructor[5] == 3:
      print("instructors course list after:", new_instructor[3][0][7],"|",new_instructor[3][1][7],"|",new_instructor[3][2][7])
    elif new_instructor[5] == 4:
      print("instructors course list after:", new_instructor[3][0][7],"|",new_instructor[3][1][7],"|",new_instructor[3][2][7],"|",new_instructor[3][3][7])

  deleter = []
  for i in range(len(instCourses)):
    for j in range(len(outputSchedules)):
      if outputSchedules[j][0] == instCourses[i][0]:
        del outputSchedules[i]
        break

  #add inst to new course
  course = course + (new_instructor,)
  outputSchedules.append(course)

  courseQueue = courseQueue + instCourses
  return [new_instructor,courseQueue]

#####         Find all instructors with discipline overlap          #####
def newMatches(maxInstructors,course):
  maxMatchRate = 0
  MaxMatches = []
  for j, tuple in enumerate(maxInstructors):
    maxMatchRate = findMatchRate(maxInstructors[j][2],course[5])
    if maxMatchRate > 0:
      MaxMatches.append([maxInstructors[j],maxMatchRate])
  return MaxMatches

#####        Find instructor with already full class list           #####
def findNextInstructor(MaxMatches,course,courseQueue,courseindice):
  worstMatches = []
  worstMatch = None

  for k, tuple in enumerate(MaxMatches):
    if k == 0:
      worstMatch = MaxMatches[k]
      worstMatches.append(worstMatch)
    elif MaxMatches[k][1] == worstMatch[1]:
      worstMatches.append(MaxMatches[k])
    elif MaxMatches[k][1] < worstMatch[1]:
      worstMatches.clear()
      worstMatch = MaxMatches[k]
      worstMatches.append(worstMatch)
    else:
      print("in max Matches else")
  for i, tuple in enumerate(worstMatches):
    if i == 0:
      worstMatch = worstMatches[i][0]
      currentMinOverlap = findMinOverlap(worstMatches[i][0],course)
    elif currentMinOverlap < findMinOverlap(worstMatches[i][0],course):
      worstMatch = worstMatches[i][0]
  newInstAndCourse = reassignCourse(worstMatch,course,courseQueue,courseindice)
  return newInstAndCourse

#####     schduling algorithm     #####
def Scheduler(UnassignedCourseQueue,instructorQueue):
  loopBreaker = 0

  print("total Courses =", len(UnassignedCourseQueue), "| Total Instructors", len(instructorQueue))
  loopNum = len(UnassignedCourseQueue)
  courseindice = 0

  i = 0
  while len(UnassignedCourseQueue) != 0:
  #for i in range(loopNum):
    UnassignedCourseQueue[courseindice] = setPeriods(UnassignedCourseQueue[courseindice])
    matchRate = 0
    currentBestMatchRate = 0
    currentBestMatch = None
    BestMatches = []

    print(UnassignedCourseQueue[courseindice][7], "| loop #", i)
    for j, tuple in enumerate(instructorQueue):
      matchRate = findMatchRate(instructorQueue[j][2],UnassignedCourseQueue[courseindice][5])

      if matchRate > 0 and currentBestMatch == None and CheckInstSched(instructorQueue[j],UnassignedCourseQueue[courseindice]):
        currentBestMatchRate = matchRate
        BestMatches.append([instructorQueue[j], j])
      elif matchRate == currentBestMatchRate and CheckInstSched(instructorQueue[j],UnassignedCourseQueue[courseindice]):
        BestMatches.append([instructorQueue[j], j])
      elif matchRate > currentBestMatchRate and CheckInstSched(instructorQueue[j],UnassignedCourseQueue[courseindice]):
        BestMatches.clear()
        BestMatches.append([instructorQueue[j], j])


    maxMatches = newMatches(MaxLoadedInstructors,UnassignedCourseQueue[courseindice])
    if len(BestMatches) == 0 and len(MaxLoadedInstructors) > 0 and len(maxMatches) != 0:
      print("------------------------------------- Entering worst Match code ---------------------------------------------------")
      #print("ERROR: No suitable instructors for", UnassignedCourseQueue[7])
      #courseindice = courseindice + 1
      newInstAndCourse = findNextInstructor(maxMatches,UnassignedCourseQueue[courseindice],UnassignedCourseQueue,courseindice)
      UnassignedCourseQueue = newInstAndCourse[1]
      BestMatches.append(newInstAndCourse[0])
      currentBestMatch = BestMatches[0]
      print("total Courses after drop =", len(UnassignedCourseQueue), "| Total Professors below max load = ", len(instructorQueue))
      print("Match Rate:",currentBestMatchRate,"| Professor: ", currentBestMatch[0], "| load =", currentBestMatch[5])
      for k in range(len(MaxLoadedInstructors)):
        if MaxLoadedInstructors[k][0] == currentBestMatch[0]:
          MaxLoadedInstructors[k] = currentBestMatch[0]
      totalCourses = len(outputSchedules) + len(UnassignedCourseQueue)
      print("Length of output schdules =", len(outputSchedules), "| legnth of unassigned courses =", len(UnassignedCourseQueue),"| UCQ + OS =", totalCourses)
      print("------------------------------------- Exiting worst Match code ---------------------------------------------------")
    elif len(BestMatches) == 0:
      print("ERROR: No suitable instructors for", UnassignedCourseQueue[courseindice])
      courseindice = courseindice + 1
    else:
      newMatch = getRandomNum(0,len(BestMatches))
      currentBestMatch = BestMatches[newMatch][0]
      currentBestMatch = changeTupleValue(currentBestMatch,currentBestMatch[5] + 1,5)
      currentBestMatch = schedInstSched(currentBestMatch, UnassignedCourseQueue[courseindice])

      if currentBestMatch[5] == currentBestMatch[1]:
        #add instructors to full schedule list and remove from unscheduled list
        MaxLoadedInstructors.append(currentBestMatch)
        del instructorQueue[BestMatches[newMatch][1]]
      else:
        instructorQueue[BestMatches[newMatch][1]] = currentBestMatch

      UnassignedCourseQueue[courseindice] = UnassignedCourseQueue[courseindice] + (currentBestMatch,) #append instructor to course they are assigned to

      #add course to output and remove from unnassigned
      outputSchedules.append(UnassignedCourseQueue[courseindice])
      del UnassignedCourseQueue[courseindice]
      print("total Courses after drop =", len(UnassignedCourseQueue), "| Total Professors below max load = ", len(instructorQueue))

      totalCourses = len(outputSchedules) + len(UnassignedCourseQueue)
      print("Length of output schdules =", len(outputSchedules), "| legnth of unassigned courses =", len(UnassignedCourseQueue),"| UCQ + OS =", totalCourses)
      print("Match Rate:",currentBestMatchRate,"| Professor: ", currentBestMatch[0], "| load =", currentBestMatch[5])
      #print(currentBestMatch[3])

      if totalCourses > 29:
        print("\nERROR: totalCourses exceeded 29")
        break

    if courseindice == len(UnassignedCourseQueue):
      courseindice = 0
      loopBreaker = loopBreaker + 1
      if loopBreaker == 3:
        print("\n\nERROR: Caught infite loop. Some courses could not be assigned. Loop broke. \n\n")
        break


    print("")
    if i == 50:
      print("\n\nERROR: Caught infite loop. Some courses could not be assigned. Loop broke. \n\n")
      break
    else:
      i = i + 1

  #replace instance of instructors with most recent instance in courses
  all_instructors_post = instructorQueue + MaxLoadedInstructors
  for j in range(len(all_instructors_post)):
    for i in range(len(outputSchedules)):
      if all_instructors_post[j][0] == outputSchedules[i][8][0]:
        outputSchedules[i] = changeTupleValue(outputSchedules[i],all_instructors_post[j],8)
        break

  return [UnassignedCourseQueue,outputSchedules,all_instructors_post]

def main():
  All_Instructors = []
  All_Courses = []

  rows = instructors.query.all()
 # Get all the column names of the table in order to iterate through
  column_keys = instructors.__table__.columns.keys()
  # Temporary dictionary to keep the return value from table
  rows_dic_temp = {}
  rows_dic = []
  # Iterate through the returned output data set
  for row in rows:
   for col in column_keys:
    rows_dic_temp[col] = getattr(row, col)
    rows_dic.append(rows_dic_temp)
    rows_dic_temp= {}

  #go through the instructors DB and create All_Instructors from each row
  for i in range(len(rows_dic)):
    instructor = ()
    name = rows_dic[LName]
    maxload = rows_dic[MaxLoad]
    disciplines = rows_dic[Disciplines]
    courses = []
    inst_schedule = list(schedule)
    currentload = rows_dic[CurrentLoad]
    instructor = (name,maxload,disciplines,courses,inst_schedule,currentload)
    All_Instructors.append(instructor)

  ################################################################################

  rows = sections.query.all()
  # Get all the column names of the table in order to iterate through
  column_keys = sections.__table__.columns.keys()
  # Temporary dictionary to keep the return value from table
  rows_dic_temp = {}
  rows_dic = []
  # Iterate through the returned output data set
  for row in rows:
    for col in column_keys:
      rows_dic_temp[col] = getattr(row, col)
      rows_dic.append(rows_dic_temp)
      rows_dic_temp= {}

  #go through the sections DB and create All_Courses from each row
  for i in range(len(rows_dic)):
    section = ()
    code = rows_dic[Code]
    depcode = rows_dic[DepartmentCode]
    day = rows_dic[Day]
    length = rows_dic[Length]
    time = rows_dic[StartTime]
    periods = rows_dic[periods]
    name = rows_dic[Name]
    section = (code,depcode,day,length,time,periods,name)
    All_Courses.append(section)

  #Runs the scheduling algorithm and returns the two lists of assigned and Unassigned Courses
  tempList = Scheduler(All_Courses,All_Instructors)
  UnassignedCourses = tempList[0]
  AssignedCourses = tempList[1]
  instructors_list = tempList[2]

  #replace instance of instructors with most recent instance in courses

  #Appends True Or False to the instructor based on validity of solution and then puts them all in outputSchedules
  for i in range(len(AssignedCourses)):
    AssignedCourses[i] = AssignedCourses[i] + (True,)
  for i in range(len(UnassignedCourses)):
    UnassignedCourses[i] = UnassignedCourses[i] + (False,)
  outputSchedules = AssignedCourses + UnassignedCourses

  models.output_schedule.query.delete()                                         #clears outputSchedule database
  for i in range(len(outputSchedules)):                                         #loops through outputSchedulesand addes a row to the table for each
    outputSchedule = outputSchedules(Code=outputSchedules[i][0], DepartmentCode=outputSchedules[i][1], Day=outputSchedules[i][2], Length=outputSchedules[i][3], STartTime=outputSchedules[i][4], Disciplines=outputSchedules[i][5], Periods=outputSchedules[i][6], Name=outputSchedules[i][7], instructor=outputSchedules[i][8], valid=outputSchedules[i][9])
    db.session.add(outputSchedule)
    db.session.commit

  models.instructors.query.delete()                                             #clears outputSchedule database
  for i in range(len(instructors_list)):                                        #loops through outputSchedulesand addes a row to the table for each
    dayStrings = convertScheduleToStrings(instructors_list[i][4])
    inst = instructors_list(LName=instructors_list[i][0], MaxLoad=instructors_list[i][1], Disciplines=instructors_list[i][2], Course_code_1=instructors_list[i][3][0], Course_code_2=instructors_list[i][3][1], Course_code_3=instructors_list[i][3][2], Course_code_4=instructors_list[i][3][3], Schedule_Day_1=dayStrings[0], Schedule_Day_2=dayStrings[1], Schedule_Day_3=dayStrings[2], Schedule_Day_4=dayStrings[3], Schedule_Day_5=dayStrings[4], CurrentLoad=instructors_list[i][5])
    db.session.add(inst)
    db.session.commit
