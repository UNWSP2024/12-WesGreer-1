# GUI MPG Program
# Written by Wesley Greer on 4/23/2026

import tkinter
import tkinter.messagebox


# create GUI window and frames
class MyGUI:
    def __init__ (self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
# create entry spaces and buttons
        self.gallons_label = tkinter.Label(self.top_frame, text="Enter the number of gallons of gas your car holds:")
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_label = tkinter.Label(self.middle_frame, text="Enter the number of miles of your car goes on a full tank:")
        self.miles_entry = tkinter.Entry(self.middle_frame, width=10)

        self.mpg_button = tkinter.Button(self.bottom_frame, text="Calculate MPG", command= self.calculate_mpg)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command= self.main_window.destroy)
# pack everything
        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left")
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")

        self.mpg_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
# define mpg calculation function
    def calculate_mpg(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / gallons
        tkinter.messagebox.showinfo("Miles Per Gallons", mpg)


my_gui = MyGUI()
