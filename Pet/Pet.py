from functools import partial
from tkinter import *
import pyautogui
import random
import tkinter as tk
import tkinter as ttk
import time
from MongoDB_canvas import *


### this is an example, make sure it works for you and see how it works then delete
## this function adds information to mongodb then returns 2 dicts
## it takes in input from user from command line, we need to eventually change that to get that input from test file
classes_dict, assignment_dict = addPerson()
print(classes_dict,assignment_dict)


window = tk.Tk()

# Window Configuration
window.config(highlightbackground='#000')
window.overrideredirect(True)
# window.wm_attributes('-transparent', 'white')
window.wm_attributes('-transparent', True)
window.config(bg='systemTransparent')
window.attributes('-topmost', True)
# window.wm_attributes('-transparentcolor', '#000')
# might have to consult this for cross-platform transparency solution:
# https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window

# For Windos comment lines 11 - 20 and uncomment lines 23-25
# window.config(highlightbackground='black')
# window.overrideredirect(True)
# window.wm_attributes('-transparent', "black")

# Create a canvas object
canvas = tk.Canvas(window, bg='#ffffff', width=100, height=40, bd=0)
# Add a text in Canvas
myText = canvas.create_text(50, 25, text='', fill='#000', font='Helvetica 15 bold', justify='center')\

# Assign Label to Pet
label = tk.Label(window, bd=0)
label.pack()
canvas.pack()

# Assign Variables
x = 1180
cycle = 0
check = 1
category_dict = dict() # key-category string, value
task_dict = dict()
task_list = []

# Event Change
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)

# Call buddy's action .gif to an array
idle = [tk.PhotoImage(file='Animations/idle.gif', format='gif -index %i' % i) for i in
        range(5)]  # idle gif , 5 frames
idle_to_sleep = [tk.PhotoImage(file='Animations/idle_to_sleep.gif', format='gif -index %i' % i) for i in
                 range(8)]  # idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file='Animations/sleep.gif', format='gif -index %i' % i) for i in
         range(3)]  # sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file='Animations/sleep_to_idle.gif', format='gif -index %i' % i) for i in
                 range(8)]  # sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file='Animations/walking_positive.gif', format='gif -index %i' % i) for i in
                 range(8)]  # walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file='Animations/walking_negative.gif', format='gif -index %i' % i) for i in
                 range(8)]  # walk to right gif, 8 frames


# Transfer random no. to event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        # print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        # print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        if x > 0:
            check = 4
            # print('walking towards left')
            window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        if x >= 980:
            check = 5
            # print('walking towards right')
            window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
    elif event_number in sleep_num:
        check = 2
        # print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
    elif event_number == 14:
        check = 3
        # print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle


# Make the gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


# Update the Frame
def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    # walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= -3
    # walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= 3

    window.geometry('300x150+' + str(x) + '+700')
    label.configure(image=frame)
    update_clock()

    window.after(1, event, cycle, check, event_number, x)


# Update the time
def update_clock():
    curr_time = time.strftime("%H:%M")
    if curr_time == "22:54":
        canvas.itemconfig(myText, text="hellow")
    else:
        canvas.itemconfig(myText, text=curr_time)


# Allow user to add categories/courses
def add_category(category):
    print("add category")
    print(category.get())
    # add cat to the cat dict


# Allow user to add tasks to a task/assignment list
def add_task(category, task, deadline):
    print("add task")
    print(category.get())
    print(task.get())
    print(deadline.get())

    # check cat dict for a existing key, add task value to existing cat key
    # if not existing, add cat as key and add task as value
    # then add task to


# Buttons, Labels, and Entries
category = tk.StringVar()
task = tk.StringVar()
deadline = tk.StringVar()

exit_button = ttk.Button(
    window,
    text="x",
    command=lambda: window.quit(),
    cursor='hand2'
)
exit_button.place(x=0, y=0)

add_category = partial(add_category, category)
add_category_button = ttk.Button(
    window,
    text="Add Category",
    command=add_category,
    cursor='hand2'
)
add_category_button.place(x=0, y=30)

add_task = partial(add_task, category, task, deadline)
add_task_button = ttk.Button(
    window,
    text="Add Task",
    command=add_task,
    cursor='hand2'
)
add_task_button.place(x=0, y=60)


# category_label = Label(
#         window,
#         text="Category",
#         bd=4,
#         relief='ridge'
#     )
# category_label.pack(side=LEFT)
# category_label.place(x=0, y=30)


category_entry = Entry(
        window,
        textvariable=category,
        relief='ridge',
        insertofftime=600
    )
category_entry.pack(side=RIGHT)
category_entry.place(x=66, y=30)
# category_entry.focus_set()


# Loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
