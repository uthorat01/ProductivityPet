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

# Connecting to Canvas
API_URL = "https://ufl.instructure.com"

# This is an individual API key specific to each user. You can get it from your canvas account
API_KEY = "1016~Fcw98lfkis3FKV6Fzwrdcr0DKBKV0LluKPI68uCMRJbJdrW2z7ZpE4Ex2ubmQVYl"

canvas = Canvas(API_URL, API_KEY)

courseList = canvas.get_courses()

# some functions for easing interactions with Mongodb database.. sadly not all operations can be translated to functions


def getId(collection_, name):
    cursor = collection.find({})
    for collection_ in cursor:
        if collection_['name'] == name:
            return collection_['_id']


def deleteAll(collection_):
    collection_.delete_many({})

# person1 = {"name": "Michael1", "Courses" :{"CEN3031":"Period 4","PHY2049"
#             :"Period 2", "PHY2049L" : "Period 7", "CIS4930":"Period 1"}}


def createDoc(name, collection_, classes_, assignments_, assignments_dates):
    #assignment_val = {key:"date" for key in assignments_}
    assignment_val = dict(zip(assignments_,assignments_dates))
    courses_val = {key:"periodX" for key in classes_}
    person = {"name": name, "Courses" : courses_val, "Assignments" : assignment_val}
    collection_.insert_one(person)


def printAll(collection_):
    cursor = collection_.find({})
    for document in cursor:
        print(document)


def printCourses(collection_, name):
    results = collection.find({"name": name})
    print(results[0]["Courses"])   #prints "Courses" :{"CEN3031":"Period 4","PHY2049" :"Period 2", "PHY2049L" : "Period 7" ....etc


classes = []
assignments = []
assignments_date = []

for i in courseList:
    if not(hasattr(i, 'access_restricted_by_date')):

        if(i.enrollment_term_id == 2081):
            course = canvas.get_course(i.id)
            classes.append(course.course_code)
            assignmentList = course.get_assignments()
            for assignment in assignmentList:
                present = pytz.UTC.localize(datetime.now())
                if(assignment.due_at != None and present < assignment.due_at_date):
                    assi_str = str(assignment)
                    mod = assi_str[:len(assi_str) - 9]
                    assignments.append(mod)
                    assignments_date.append(assignment.due_at_date.strftime("%m/%d/%Y"))


# print("classes")
# for c in classes:
#     print(c)
#     # print(type(c))
# print("Assignments")
# for a in assignments:
#     print(a)
#     # print(type(a))
# for b in assignments_date:
#     print(b)

createDoc("Michael", collection, classes, assignments, assignments_date)

#printCourses(collection, "Michael")
#deleteAll(collection)