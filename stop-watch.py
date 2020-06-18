from tkinter import *
from datetime import datetime

counter = 66600
running = False


def counterfunc(label):
    def count():
        if running:
            global counter
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
            label['text'] = display
            label.after(1000, count)
            counter += 1
        
    count()

def start(label):
    global running
    running = True
    counterfunc(label)
    start_button['state'] = 'disabled'
    stop_button['state'] = 'normal'
    reset_button['state'] = 'normal'
    
def stop():
    global running
    running = False
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'
    reset_button['state'] = 'normal'
    
def reset(label):
    global counter
    counter = 66600
    if running == False:
        reset_button['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'
        

root = Tk()
label = Label(root, text = "Welome!", fg = 'black')
button_frame = Frame(root)
start_button = Button(button_frame, text = "Start",command = lambda:start(label))
stop_button = Button(button_frame, text = "Stop",command = stop)
reset_button = Button(button_frame, text = "Reset",command = lambda:reset(label))
label.grid(row = 0, column = 0, sticky = 'news')
button_frame.grid(row = 1, column = 0, sticky = 'news')
start_button.grid(row = 0, column = 0)
stop_button.grid(row = 0, column = 1)
reset_button.grid(row = 0, column = 2)
root.mainloop()
    

