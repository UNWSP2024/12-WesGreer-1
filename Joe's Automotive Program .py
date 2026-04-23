# Checkbox Program
# Written By Wesley Greer on 4/23/2026

import tkinter

class MyGUI:
    def __init__(self):
# create window and frames
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
# create the checkbuttons
        self.auto1 = tkinter.IntVar()
        self.auto2 = tkinter.IntVar()
        self.auto3 = tkinter.IntVar()
        self.auto4 = tkinter.IntVar()
        self.auto5 = tkinter.IntVar()
        self.auto6 = tkinter.IntVar()
        self.auto7 = tkinter.IntVar()

        self.auto1.set(0)
        self.auto2.set(0)
        self.auto3.set(0)
        self.auto4.set(0)
        self.auto5.set(0)
        self.auto6.set(0)
        self.auto7.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Oil Change-$30", variable=self.auto1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Lube Job-$20", variable=self.auto2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Radiator Flush-$40", variable=self.auto3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text="Transmission Fluid-$100", variable=self.auto4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text="Inspection-$35", variable=self.auto5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text="Muffler replacement-$200", variable=self.auto6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text="Tire Rotation-$20", variable=self.auto7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
# use label to display total
        self.desc_label = tkinter.Label(self.mid_frame, text = 'Your total is: $')
        self.value = tkinter.StringVar()
        self.total_label = tkinter.Label(self.mid_frame, textvariable = self.value)

        self.desc_label.pack(side="left")
        self.total_label.pack(side="left")
# make buttons for calculation and exit
        self.calc_button = tkinter.Button(self.bottom_frame, text="Calculate Total", command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()
# define the calculate function
    def calculate(self):
        total = 0
        if self.auto1.get() == 1:
            total += 30
        if self.auto2.get() == 1:
            total += 20
        if self.auto3.get() == 1:
            total += 40
        if self.auto4.get() == 1:
            total += 100
        if self.auto5.get() == 1:
            total += 35
        if self.auto6.get() == 1:
            total += 200
        if self.auto7.get() == 1:
            total += 20

        self.value.set(total)

my_gui = MyGUI()
