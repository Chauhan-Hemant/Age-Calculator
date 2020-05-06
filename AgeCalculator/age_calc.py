from tkinter import *
from tkinter import messagebox

# functions to clear all the values
def clearAll():
    day_Field.delete(0, END)
    month_Field.delete(0, END)
    year_Field.delete(0, END)

    given_Day_Field.delete(0, END)
    given_Month_Field.delete(0, END)
    given_Year_Field.delete(0, END)

    result_Day_Field.delete(0, END)
    result_Month_Field.delete(0, END)
    result_Year_Field.delete(0, END)


# function to check error
def checkError():
    if (day_Field.get() == "" or month_Field.get() == ""
            or year_Field.get() == "" or given_Day_Field.get() == ""
            or given_Month_Field.get() == "" or given_Year_Field.get() == ""):
        messagebox.showerror("Input Error")
        clearAll()
        return -1


# function to calculate age
def calculateAge():
    value = checkError()

    # to check empty fields
    if value == -1:
        return
    else:
        birth_day = int(day_Field.get())
        birth_month = int(month_Field.get())
        birth_year = int(year_Field.get())

        given_day = int(given_Day_Field.get())
        given_month = int(given_Month_Field.get())
        given_year = int(given_Year_Field.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # if birth day is greater than given birth_day
        # then add 30 to the date and subtract 1 month
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        # if birth month is greater than given birth_month
        # then add 12 to the month and subtract 1 year
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12

        # calculate day month year
        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        result_Day_Field.insert(10, str(calculated_day))
        result_Month_Field.insert(10, str(calculated_month))
        result_Year_Field.insert(10, str(calculated_year))

        total_Age.insert(20, str(calculated_year) +" Years " + str(calculated_month) +" Months " + str(calculated_day) +" Days")


if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light grey")

    # set the name of tkinter GUI Window
    gui.title("Age Calculator")

    # set the Default GUI window resolution
    gui.geometry("715x250")

    date_of_birth = Label(gui, text="Date Of Birth", bg="Light grey")

    givenDate = Label(gui, text="Given Date", bg="Light grey")

    day = Label(gui, text="Day", bg="light grey")
    month = Label(gui, text="Month", bg="Light grey")
    year = Label(gui, text="Year", bg="Light grey")

    givenDay = Label(gui, text="Given Day", bg="Light grey")
    givenMonth = Label(gui, text="Given Month", bg="Light grey")
    givenYear = Label(gui, text="Given Year", bg="Light grey")

    resultDay = Label(gui, text="Days                 ==>", bg="Light grey")
    resultMonth = Label(gui, text="Months              ==>", bg="Light grey")
    resultYear = Label(gui, text="Years                 ==>", bg="Light grey")
    final_age = Label(gui, text="Final Age          ==>", bg="Light grey")

    resultantAge = Button(gui, text="Resultant Age", fg="Black", bg="green", command=calculateAge)

    clearAllEntry = Button(gui, text="Clear All", fg="Black", bg="orange", command=clearAll)

    day_Field = Entry(gui)
    month_Field = Entry(gui)
    year_Field = Entry(gui)

    given_Day_Field = Entry(gui)
    given_Month_Field = Entry(gui)
    given_Year_Field = Entry(gui)

    result_Day_Field = Entry(gui)
    result_Month_Field = Entry(gui)
    result_Year_Field = Entry(gui)

    total_Age = Entry(gui, width=30)

    date_of_birth.grid(row=0, column=1)

    day.grid(row=1, column=0)
    day_Field.grid(row=1, column=1)

    month.grid(row=2, column=0)
    month_Field.grid(row=2, column=1)

    year.grid(row=3, column=0)
    year_Field.grid(row=3, column=1)

    givenDate.grid(row=0, column=4)

    givenDay.grid(row=1, column=3)
    given_Day_Field.grid(row=1, column=4)

    givenMonth.grid(row=2, column=3)
    given_Month_Field.grid(row=2, column=4)

    givenYear.grid(row=3, column=3)
    given_Year_Field.grid(row=3, column=4)

    resultantAge.grid(row=4, column=2)

    resultYear.grid(row=5, column=1)
    result_Year_Field.grid(row=5, column=2)

    resultMonth.grid(row=6, column=1)
    result_Month_Field.grid(row=6, column=2)

    resultDay.grid(row=7, column=1)
    result_Day_Field.grid(row=7, column=2)

    final_age.grid(row=8, column=1)
    total_Age.grid(row=8, column=2)

    clearAllEntry.grid(row=9, column=2)

    gui.mainloop()
