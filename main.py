import time
from tkinter import *
from tkinter import ttk

########################################################################################################################
# test scale
########################################################################################################################
test = Tk()
test.title('Test')
scalenum=DoubleVar()
test_scale = Scale(test, from_=0, to=400, length=140, orient=VERTICAL, variable=scalenum).pack()

rpmA = int()
depth = int()
########################################################################################################################


# MINOR DISPLAY SETUP ITEMS
root = Tk()  # initialize root variable
root.geometry("800x480")  # root sized to hdmi monitor
root.title('Nautilus HUD')


# STYLE CONFIGURATION
root.style = ttk.Style(root)
root.style.configure('title.TLabel', font=('Times', 14, 'bold')) # For gauge labels
root.style.configure('.TLabel', font=('Times', 14)) # gauge readings

# GRID MANAGEMENT (2x3)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=2)

# HEADING DISPLAY SETUP
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

# DEPTH DISPLAY SETUP
# labels
depth_label = ttk.Label(root, text='DEPTH', style='title.TLabel').grid(column=1, row=0, sticky='n')
# canvas items
depth_canvas = Canvas(root, height=400, width=100)
depth_canvas.create_rectangle(3, 400, 100, 3, width='3')
depth_canvas.grid(column=1, row=1, rowspan=2)
depth_bar = depth_canvas.create_rectangle(3, 400, 100, depth, fill='#FFCC00')

# RPM DISPlAY SETUP
#labels
RPM_label = ttk.Label(root, text='RPM', style='title.TLabel').grid(column=0, row=2, sticky="nw")
# canvas items
RPM_canvas = Canvas(root, height=100, width=550)
RPM_canvas.create_rectangle(550, 3, 3, 100, width='3')
RPM_bar = RPM_canvas.create_rectangle(rpmA, 3, 3, 100, fill='#FFCC00')
RPM_canvas.grid(column=0, row=2)


# DYNAMIC ELEMENTS LOOP
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

