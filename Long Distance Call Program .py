# Rate Calculation Program
# Written By Wesley Greer on 4/24/2026

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
# Create frames
        self.top_frame = tkinter.Frame(self.mainwindow)
        self.mid_frame = tkinter.Frame(self.mainwindow)
        self.bottom_frame = tkinter.Frame(self.mainwindow)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
# display rates
        self.rate_label = tkinter.Label(self.top_frame, text = """Daytime- $0.02 per minute
Evening- $0.12 per minute
Off-Peak- $0.05 per minute""")

        self.rate_label.pack()
# create radiobuttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Daytime (6:00 A.M. through 5:59 P.M.)', variable = self.radio_var, value = 1)

        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Evening (6:00 P.M.  through 11:59 P.M.)', variable = self.radio_var, value = 2)

        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Off-Peak (midnight through 5:59 P.M.)', variable = self.radio_var, value = 3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
# create entry label and widget
        self.entry_label = tkinter.Label(self.mid_frame, text = "Enter the number of minutes of your call:")
        self.entry_label.pack(side="left")
      
        self.time_entry = tkinter.Entry(self.mid_frame, width = 10)
        self.time_entry.pack(side="left")
# create buttons for entry and exit
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Calculate Total', command = self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.mainwindow.destroy)

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.mainwindow.mainloop()
# define calculate function
    def calculate(self):
        if self.radio_var.get() == 0:
            tkinter.messagebox.showinfo(message = "You must select a rate to calculate the total charge.")
        if self.radio_var.get() == 1:
            total = .02 * float(self.time_entry.get())
            tkinter.messagebox.showinfo(message = "The total charge is: $" + str(f"{total:.2f}"))
        if self.radio_var.get() == 2:
            total = .12 * float(self.time_entry.get())
            tkinter.messagebox.showinfo(message = "The total charge is: $" + str(f"{total:.2f}"))
        if self.radio_var.get() == 3:
            total = .05 * float(self.time_entry.get())
            tkinter.messagebox.showinfo(message = "The total charge is: $" + str(f"{total:.2f}"))

my_gui = MyGUI()
