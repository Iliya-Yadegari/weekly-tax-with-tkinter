from tkinter import *
import sys

def tax_cal(hourEntered_e):
     grossPay = int(hourEntered_e) * 15
     
     if grossPay < 450:
         messagebox.showerror('Error','You have not earned enough to be taxed properly.')
         
     else:
         grossRemaining = grossPay - 37.4 - 45
         
         grossRemainingTax = grossRemaining * 0.3
         
         totalTax = 37.4 + 45 + grossRemainingTax
         
         netPay = grossPay - totalTax
         
         messagebox.showinfo('Result',f'Your gross pay is {grossPay}, your total tax is {totalTax}, your net pay is {netPay}.')