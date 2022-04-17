import random
import time
import tkinter as tk
import tkinter as ttk
from Backend.MongoDB_canvas import *
from functools import partial
from tkinter import *


window = tk.Tk()

# Window Configuration
window.config(highlightbackground='#000')
window.overrideredirect(True)
window.wm_attributes('-transparent', True)
window.config(bg='systemTransparent')
window.attributes('-topmost', True)
# window.wm_attributes('-transparentcolor', '#000')
# might have to consult this for cross-platform transparency solution:
# https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window

# For Windows comment lines 12 - 20 and uncomment lines 23-25
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
category_dict = dict()  # key-category string, value-period/time
task_dict = dict()  # key-task string, value-deadline string
task_list = []  # organize the tasks into a list by deadline

# this is an example, make sure it works for you and see how it works then delete
# this function adds information to mongodb then returns 2 dicts
# it takes in input from user from command line, we need to eventually change that to get that input from test file

# category_dict, task_dict = addPerson()
# print(category_dict, task_dict)


# Event Change
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)

# Call buddy's action .gif to an array
idle = [tk.PhotoImage(file='Pet/Animations/idle.gif', format='gif -index %i' % i) for i in
        range(5)]  # idle gif , 5 frames
idle_to_sleep = [tk.PhotoImage(file='Pet/Animations/idle_to_sleep.gif', format='gif -index %i' % i) for i in
                 range(8)]  # idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file='Pet/Animations/sleep.gif', format='gif -index %i' % i) for i in
         range(3)]  # sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file='Pet/Animations/sleep_to_idle.gif', format='gif -index %i' % i) for i in
                 range(8)]  # sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file='Pet/Animations/walking_positive.gif', format='gif -index %i' % i) for i in
                 range(8)]  # walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file='Pet/Animations/walking_negative.gif', format='gif -index %i' % i) for i in
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


# # Allow user to add categories/courses
# def add_category(category):
#     print("add category")
#     print(category.get())
#     # add cat to the cat dict
#     category_dict.update({str(category.get()) : ""})
#     print (category_dict)


def options():
    task_var = tk.StringVar()
    deadline_var = tk.StringVar()
    canvas_api_key_var = tk.StringVar()

    options_window = Toplevel(window)
    options_window.geometry('400x200+100+200')
    options_window.title("Options")

    # Option window - create filler for empty 0th row
    options_window.grid_rowconfigure(0, minsize=10)

    # Option window - adding tasks and deadlines
    task_label = tk.Label(options_window, text="Task")
    task_label.grid(row=1, column=0, sticky=E)

    deadline_label = tk.Label(options_window, text="Deadline")
    deadline_label.grid(row=2, column=0, sticky=E)

    task_entry = tk.Entry(options_window, textvariable=task_var, relief='ridge', insertofftime=600)
    task_entry.grid(row=1, column=1)

    deadline_entry = tk.Entry(options_window, textvariable=deadline_var, relief='ridge', insertofftime=600)
    deadline_entry.grid(row=2, column=1)

    add_task_button = ttk.Button(options_window, text="Add Task", command=partial(add_task, task_var, deadline_var), cursor='hand2')
    add_task_button.grid(row=2, column=2, sticky=W)

    # Create filler for empty 3rd row
    options_window.grid_rowconfigure(3, minsize=10)

    # Option window - Ask for API key for Canvas linking
    canvas_api_key_label = tk.Label(options_window, text="Canvas API Key")
    canvas_api_key_label.grid(row=4, column=0, sticky=E)

    canvas_api_key_entry = tk.Entry(options_window, textvariable=canvas_api_key_var, relief='ridge', insertofftime=600)
    canvas_api_key_entry.grid(row=4, column=1)

    connect_to_canvas_button = ttk.Button(options_window, text="Connect to Canvas", command=partial(connect_to_canvas, canvas_api_key_var), cursor='hand2')
    connect_to_canvas_button.grid(row=4, column=2, sticky=W)


# Add tasks to a task/assignment list
def add_task(task, deadline):
    print("add task")

    task_dict.update({task.get(): deadline.get()})
    print(task_dict)


def connect_to_canvas(canvas_api_key):
    addPerson(canvas_api_key.get())


# Buttons, Labels, and Entries
# category = tk.StringVar()
# task = tk.StringVar()
# deadline = tk.StringVar()
# canvas_api_key = tk.StringVar()


# Buttons, Labels, and Entries
options_button = ttk.Button(
    window,
    text="Options",
    command=options,
    cursor='hand2'
)
# options_button.pack()
options_button.place(x=0, y=0)

exit_button = ttk.Button(
    window,
    text="Exit",
    command=lambda: window.quit(),
    cursor='hand2'
)
# exit_button.pack()
exit_button.place(x=0, y=30)


# Loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
