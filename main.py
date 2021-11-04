import time
# import RPi.GPIO as gpio
from tkinter import *
from tkinter import ttk


#####
# test scale
#####
test = Tk()
test.title('Test')
scalenum=DoubleVar()
test_scale = Scale(test, from_=0, to=400, length=140, orient=VERTICAL, variable=scalenum).pack()



# gpio.setmod(gpio.BCM)

# dataINA = int() # Proximity sensor input A (PSA)
#gpio.setup( , gpio.IN) TODO: find IO pins
# dataINB = int() # Proximity sensor input B (PSB)
#gpio.setup( , gpio.IN) TODO: find IO pins
# dataINC = int() # Pressure sensor input C (PSC)
# dataIND = int() # Pressure sensor input D (PSD)

rpmA = int() # RPM from sensor A value
# rpmB = int() # RPM from sensor B value
# avg_rpm = int() # (RPMA-RPMB)/ 2
# depth_meters = float() # Depth taken from pressure sensor data

# prevmillis = float() # to store time
# duration = float() # to store time difference
# refresh = float() # to store time fo refresh of reading

# currentstateA = bool() # Current state of PSA input scan
# prevstateA = bool() # State of PSA sensor in previous scan

# currentstateB = bool() # Current state of PSB input scan
# prevstateB = bool() # State of PSB sensor in previous scan

########################################################################################################################
# RPM SENSOR
########################################################################################################################

# def RPM():
#  currentstateA = gpio.input(dataINA)
#    if(prevstateA != currentstateA):
#        if (currentstateA == True):
#             return duration=((time.time()/1000) - prevmillis)
#            return rpmA=(60000000/duration)
#             return prevmillis=time.time()
#         else:
#             return rpmA=0;
#     pass


########################################################################################################################
# DEPTH SENSOR
########################################################################################################################
depth =int(0)
########################################################################################################################
# HUD
########################################################################################################################

# MINOR DISPLAY SETUP ITEMS
root = Tk()  # initialize root variable
root.geometry("800x480")  # root sized to hdmi monitor
root.title('Nautilus HUD')


# STYLE CONFIGURATION
root.style = ttk.Style(root)
root.style.configure('title.TLabel', font=('Times', 14, 'bold'))
root.style.configure('.TLabel', font=('Times', 14))

# GRID MANAGEMENT
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=2)

# HEADING DISPLAY
# labels
heading_label = ttk.Label(root, text='HEADING', style='title.TLabel').grid(column=0, row=0, sticky='n')

heading_up = ttk.Label(root, text='UP', style='.TLabel').grid(column=0, row=1, sticky='n')
heading_port = ttk.Label(root, text='PORT', style='.TLabel').grid(column=0, row=1, sticky='w', padx=100)
heading_starboard = ttk.Label(root, text='STARBOARD', style='.TLabel').grid(column=0, row=1, sticky='e', padx=40)
heading_down = ttk.Label(root, text='DOWN', style='.TLabel').grid(column=0, row=1, sticky='s')

# canvas items
heading_canvas = Canvas(root, height=250, width=300)
heading_canvas.create_oval(25, 3, 275, 250, width='3')
heading_canvas.create_line(25, 125, 275, 125, width='3')
heading_canvas.create_line(150, 0, 150, 250, width='3')
heading_arrow = heading_canvas.create_line(150, 125, 150, 0, fill='#FFCC00', width='5',arrow='last')
heading_canvas.grid(column=0, row=1)

# DEPTH DISPLAY
depth_label = ttk.Label(root, text='DEPTH', style='title.TLabel').grid(column=1, row=0, sticky='n')
depth_value = ttk.Label(root, text=str(depth), style='.TLabel').place(x=730, y=25, anchor='n')

# canvas items
depth_canvas = Canvas(root, height=400, width=100)
depth_canvas.create_rectangle(3, 400, 100, 3, width='3')
depth_canvas.grid(column=1, row=1, rowspan=2)
depth_bar = depth_canvas.create_rectangle(3, 400, 100, depth, fill='#FFCC00')

# RPM DISPlAY
RPM_label = ttk.Label(root, text='RPM', style='title.TLabel').grid(column=0, row=2, sticky="nw")

RPM_value = ttk.Label(root, text=rpmA, style='.TLabel').place(x=20, y=410, anchor='w')

# canvas items
RPM_canvas = Canvas(root, height=100, width=550)
RPM_canvas.create_rectangle(550, 3, 3, 100, width='3')
RPM_bar = RPM_canvas.create_rectangle(250, 3, 3, 100, fill='#FFCC00') #int value 250 should be replaced for rpm sensor out of total range
RPM_canvas.grid(column=0, row=2)

# USED TO EDIT THE ARROW POSITION
#
#heading_canvas.coords(heading_arrow, 150, 125, x coordinate, y coordniate) # replace variables with appropriate
#root.update()
#time.sleep(1)



while True:
    # depth elements
    depth = int(scalenum.get())
    depth_canvas.coords(depth_bar, 3, 400, 100, depth)
    depth_value = ttk.Label(root, text=str(depth), style='.TLabel').place(x=730, y=25, anchor='n')

    # rpm elements
    rpmA = int(scalenum.get())
    RPM_canvas.coords(RPM_bar, rpmA, 3, 3, 100)
    RPM_value = ttk.Label(root, text=rpmA, style='.TLabel').place(x=20, y=410, anchor='w')


    # heading elements
    heading_x = int(scalenum.get())
    heading_y = int(scalenum.get())
    heading_canvas.coords(heading_arrow, 150, 125, heading_x, heading_y)
    time.sleep(0.01)
    root.update()


root.mainloop()  # run hud
test.mainloop()

