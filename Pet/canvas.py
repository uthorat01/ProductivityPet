from canvasapi import Canvas

API_URL = "https://ufl.instructure.com"

API_KEY = "insertKeyHere"

canvas = Canvas(API_URL, API_KEY)

courseList = canvas.get_courses()
print(courseList[0])

course = canvas.get_course(452971)
print(course.name)