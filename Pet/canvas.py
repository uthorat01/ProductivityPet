from canvasapi import Canvas

API_URL = "https://ufl.instructure.com"

API_KEY = "insertKey"

canvas = Canvas(API_URL, API_KEY)

courseList = canvas.get_courses()
print(courseList[0])


for i in courseList:
    if not(hasattr(i, 'access_restricted_by_date')):
        print(i)
