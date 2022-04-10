from canvasapi import Canvas

from datetime import datetime
import pytz

API_URL = "https://ufl.instructure.com"

API_KEY = "insertKey"

canvas = Canvas(API_URL, API_KEY)

courseList = canvas.get_courses()

for i in courseList:
    if not(hasattr(i, 'access_restricted_by_date')):

        if(i.enrollment_term_id == 2081):
            course = canvas.get_course(i.id)
            print("\n" + course.course_code + "\n")
            assignmentList = course.get_assignments()
            for assignment in assignmentList:
                #present = datetime.now()
                present = pytz.UTC.localize(datetime.now())
                if(assignment.due_at != None and present < assignment.due_at_date):
                    print(assignment)

    #get classes, assignments, and periods
