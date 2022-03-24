# Import Modules
import pyautogui
import random
import tkinter as tk

# Assign Variables
x = 1280
cycle = 0
check = 1

# window = tk.Tk()

# Event Change
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)


# impath = '//Users/yannalin/Documents/csprojects/GitHub/CEN3031Project/'



# transfer random no. to event
def event(cycle, check, event_number, x):
    print(check)
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
        phrase1 = 'idle'
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
        phrase1 = 'from idle\n to sleep'
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
        phrase1 = 'walking \ntowards right'
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
        phrase1 = 'walking \ntowards left'
    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
        phrase1 = 'sleep'
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle
        phrase1 = 'from sleep\n to idle'
    # canvas.create_text(50, 25, text= phrase1, fill="white", font=('Helvetica 7 bold'))
    print("changing text")
    canvas.itemconfig(myText, text= phrase1)



# Make it Alive!
# make the gif work
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

    window.geometry('100x150+' + str(x) + '+800')
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)


window = tk.Tk()

# call buddy's action .gif to an array
idle = [tk.PhotoImage(file='Animations/idle.gif', format='gif -index %i' % (i)) for i in
        range(5)]  # idle gif , 5 frames
idle_to_sleep = [tk.PhotoImage(file='Animations/idle_to_sleep.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file='Animations/sleep.gif', format='gif -index %i' % (i)) for i in
         range(3)]  # sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file='Animations/sleep_to_idle.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file='Animations/walking_positive.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file='Animations/walking_negative.gif', format='gif -index %i' % (i)) for i in
                 range(8)]  # walk to right gif, 8 frames

# idle = [tk.PhotoImage(file=impath+'Animations/idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif , 5 frames
# idle_to_sleep = [tk.PhotoImage(file=impath+'Animations/idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif, 8 frames
# sleep = [tk.PhotoImage(file=impath+'Animations/sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif, 3 frames
# sleep_to_idle = [tk.PhotoImage(file=impath+'Animations/sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif, 8 frames
# walk_positive = [tk.PhotoImage(file=impath+'Animations/walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif, 8 frames
# walk_negative = [tk.PhotoImage(file=impath+'Animations/walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif, 8 frames

# window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)
#window.wm_attributes('-transparent', "white")
window.wm_attributes('-transparent', "black")
# window.wm_attributes('-transparentcolor', 'black')
## might have to consult this for cross-platform transparency solution: https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window

# assign label to cat
label = tk.Label(window, bd=0, bg='black')
label.pack()

#Create a canvas object
canvas= tk.Canvas(window, width= 100, height= 75, bg= 'black')
#Add a text in Canvas
myText = canvas.create_text(50, 25, text= '', fill="white", font=('Helvetica 7 bold'))
canvas.pack()

# loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
