from canvasapi import Canvas
import pymongo
from pymongo import MongoClient
from datetime import datetime
import pytz

# Connecting to the MongoDB cluster. ADMIN and ADMIN are the username/password I created for the cluster
client = pymongo.MongoClient("mongodb+srv://ADMIN:ADMIN@cen-project.mj6mb.mongodb."
                             "net/Test?retryWrites=true&w=majority")

# Entering the Pet_Project database
db = client["Pet_Project"]

# Entering the Students Collection
collection = db["Students"]

# Translation of period to time
schedule_time = {1: '7:25', 2: '8:30', 3: '9:35', 4: '10:40', 5: '11:45', 6: '12:50', 7: '1:55', 8: '3:00', 9: '4:05'}


# # Connecting to Canvas
# API_URL = "https://ufl.instructure.com"
#
# # This is an individual API key specific to each user. You can get it from your canvas account
# API_KEY = ""
#
# canvas = Canvas(API_URL, API_KEY)
#
# courseList = canvas.get_courses()

# some functions for easing interactions with Mongodb database.. sadly not all operations can be translated to functions


def getId(collection_, name):
    cursor = collection.find({})
    for collection_ in cursor:
        if collection_['name'] == name:
            return collection_['_id']


def deleteAll(collection_):
    collection_.delete_many({})


def createDoc(name, collection_, classes_, assignments_, assignments_dates, classes_times):
    assignment_val = dict(zip(assignments_, assignments_dates))
    courses_val = dict(zip(classes_, classes_times))
    person = {"name": name, "Courses": courses_val, "Assignments": assignment_val}
    collection_.insert_one(person)
    return courses_val, assignment_val


def printAll(collection_):
    cursor = collection_.find({})
    for document in cursor:
        print(document)


def printCourses(collection_, name):
    results = collection.find({"name": name})
    print(results[0][
              "Courses"])  # prints "Courses" :{"CEN3031":"Period 4","PHY2049" :"Period 2", "PHY2049L" : "Period 7" ....etc


def getCourses(classes):
    name = input("Please input your name ")
    classes_time = []
    for i in range(len(classes)):
        period = input("Please enter the period # for " + classes[i] + ' ')
        classes_time.append(schedule_time[int(period)])
    return classes_time, name


def addPerson():
    classes = []
    assignments = []
    assignments_date = []

    API_URL = "https://ufl.instructure.com"
    canvas_key = input("Please input your canvas key ")
    API_KEY = canvas_key
    canvas = Canvas(API_URL, API_KEY)
    courseList = canvas.get_courses()
    for i in courseList:
        if not (hasattr(i, 'access_restricted_by_date')):

            if i.enrollment_term_id == 2081:
                course = canvas.get_course(i.id)
                classes.append(course.course_code)
                assignmentList = course.get_assignments()
                for assignment in assignmentList:
                    present = pytz.UTC.localize(datetime.now())
                    if assignment.due_at != None and present < assignment.due_at_date:
                        assi_str = str(assignment)
                        mod = assi_str[:len(assi_str) - 9]
                        assignments.append(mod)
                        assignments_date.append(assignment.due_at_date.strftime("%m/%d/%Y"))
    classes_time, name = getCourses(classes)
    createDoc(name, collection, classes, assignments, assignments_date, classes_time)
    return courses_dict,assignments_dict

# addPerson is a function that connects to convas. It asks user to unput their canvas API key, name and period for each class.
#it will add this information to mongodb and also returns 2 dicts. 
#courses dict looks like this CEN3031:11:45, CIS4930: 12:45 .... assignment_dict looks like this Sprint1 : 11/04/22
  
courses_dict, assignment_dict = addPerson()

