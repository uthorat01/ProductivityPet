import unittest
from canvasapi import Canvas

class MyTestCase(unittest.TestCase):

    def setUp(self):
        API_URL = "https://ufl.instructure.com"

        API_KEY = "insertKey"

        self.canvas = Canvas(API_URL, API_KEY)

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


if __name__ == '__main__':
    unittest.main()
