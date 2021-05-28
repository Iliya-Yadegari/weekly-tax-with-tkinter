from tkinter import *
import weeklyTaxModule as wtm

window = Tk()

hourEntered_lbl = Label(window,text = 'Enter the number of hours you have worked this week ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
hourEntered_ent = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = lambda: wtm.tax_cal(hourEntered_ent.get())).grid(row = 1, column = 0, padx = 10, pady = 10)

hourEntered_ent.grid(row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()