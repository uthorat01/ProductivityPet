import unittest
from canvasapi import Canvas
import random
import string
import MongoDB_canvas
import pymongo
from pymongo import MongoClient
from datetime import datetime
import pytz

class MyTestCase(unittest.TestCase):
    API_KEY = "insertKey"
    def setUp(self):
        API_URL = "https://ufl.instructure.com"

        self.canvas = Canvas(API_URL, self.API_KEY)

        self.courseList = self.canvas.get_courses()
        self.newCourseList = []
        self.assignmentList = []
        for i in self.courseList:
            if not (hasattr(i, 'access_restricted_by_date')):
                if (i.enrollment_term_id == 2081):
                    self.newCourseList.append(i)
                    course = self.canvas.get_course(i.id)

                    assignmentList = course.get_assignments()
                    self.assignmentList.append(course.get_assignments())
        self.client = pymongo.MongoClient("mongodb+srv://ADMIN:ADMIN@cen-project.mj6mb.mongodb."
                                          "net/Test?retryWrites=true&w=majority")

        self.db = self.client["Pet_Project"]


        self.collection = self.db["Students"]


    def test_course_list_not_empty(self):
        self.assertTrue(self.newCourseList)

    def test_assignment_list_not_empty(self):
        self.assertTrue(self.assignmentList)

    def test_correct_course_year(self):
        failures = []
        for course in self.newCourseList:
            if course.start_at_date.year != 2022:
                failures.append(course)

        self.assertEqual([], failures)

    def test_add_person(self):
        #letters = string.digits
        #randomName = ''.join(random.choice(letters) for i in range(10))
        courses_dict, assignments_dict = MongoDB_canvas.addPerson(self.API_KEY)
        self.name = input("Please enter your name again: ")
        courses, assi = MongoDB_canvas.getCourses_Assignments(MongoDB_canvas.collection, self.name)
        self.assertTrue(courses)
        self.assertTrue(assi)

    def test_id(self):
        self.name = input("Please enter your name again: ")
        id = MongoDB_canvas.getId(MongoDB_canvas.collection, self.name)
        self.assertTrue(id)

    def test_z_database_empty(self):
        MongoDB_canvas.deleteAll(MongoDB_canvas.collection)
        cursor = MongoDB_canvas.collection.find({})
        failures = []
        for document in cursor:
            failures.append(course)

        self.assertEqual([], failures)


if __name__ == '__main__':
    unittest.main()
