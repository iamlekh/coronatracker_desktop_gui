from tkinter import *
from datetime import datetime
from PIL import Image
import json
import requests
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

###########################################################

resp = requests.get("https://api.covid19india.org/data.json")
info = resp
info = json.loads(info.text)
totalconfirmed = info["cases_time_series"][-1]['totalconfirmed']
totaldeceased = info["cases_time_series"][-1]['totaldeceased']
totalrecovered = info["cases_time_series"][-1]['totalrecovered']
date = info["cases_time_series"][-1]['date']

df = pd.DataFrame(info["cases_time_series"])
df['dailyconfirmed'] = pd.to_numeric(df['dailyconfirmed'],downcast='integer')
x = df.index
y =  df['dailyconfirmed']


###########################################################



time = datetime.now()

col1 = '#ffffff' #white
col2 = '#000000' #black
col3 = '#78dedc' #bg
col4 = '#33b6de' # blue
col5 = '#3ad638' #green
col6 = '#e6173d' #red
col7 =  '#8f8f8f' #grey
app = Tk()

app.geometry('1000x600')
app.resizable(width=0, height=0)
app.title("CV tracker")

photo = PhotoImage(file = "icons8-coronavirus-50.png")
app.iconphoto(False, photo)

#app.iconbitmap("icons8-coronavirus-50.png")
app.configure(bg = col1)




name_frame = Frame(app, width = 2000, height = 50, bg = col3, relief = 'flat')
name_frame.grid(row = 0, column = 0, columnspan = 3, sticky = NSEW)

infected_frame = Frame(app, width = 300, height = 100,  bg = col6, relief = 'flat')
infected_frame.grid(row = 1, column = 0,sticky = NW, pady = 5,  padx = 5)

rec_frame = Frame(app, width = 300, height = 100,  bg = col5, relief = 'flat')
rec_frame.grid(row = 1, column = 1,sticky = NW, pady = 5,  padx = 5)

death_frame = Frame(app, width = 300, height = 100,  bg = col7, relief = 'flat')
death_frame.grid(row = 1, column = 2,sticky = NW, pady = 5)

foot_frame = Frame(app, width = 1000, height = 50, bg = col3, relief = 'flat')
foot_frame.place(x = 1, y = 550)
###############################################################


app_name = Label(name_frame, text= "CORONAVIRUS CASES IN INDIA TILL {} 2020".format(date.upper()), width = 50, height  = 1, pady = 20,padx = 0, relief = "flat", anchor = CENTER, font = ("arial 25 bold"), bg = col3, fg = col1)
app_name.grid(row = 0, column = 0, pady = 10,padx = 0)

inf_name = Label(infected_frame, text= "infected", width = 30, height  = 2, pady = 10 ,padx = 0, relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col6, fg = col1)
inf_name.grid(row = 0, column = 0, pady = 2, padx = 19)
inf_COUNT = Label(infected_frame, text= totalconfirmed, width = 7, height  = 1, pady = 10, padx = 0,relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col6, fg = col1)
inf_COUNT.grid(row = 1, column = 0, pady = 1, padx = 1)

rec_name = Label(rec_frame, text= "recovered", width = 30, height  = 2, pady = 10 ,padx = 0, relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col5, fg = col1)
rec_name.grid(row = 0, column = 1, pady = 2, padx = 19)
rec_COUNT = Label(rec_frame, text= totalrecovered, width = 7, height  = 1, pady = 10, padx = 0,relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col5, fg = col1)
rec_COUNT.grid(row = 1, column = 1, pady = 1, padx = 1)


ded_name = Label(death_frame, text= "dead", width = 30, height  = 2, pady = 10 ,padx = 0, relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col7, fg = col1)
ded_name.grid(row = 0, column = 2, pady = 2, padx = 19)
ded_COUNT = Label(death_frame, text= totaldeceased, width = 7, height  = 1, pady = 10, padx = 0,relief = "flat", anchor = CENTER, font = ("courier 15 bold"), bg = col7, fg = col1)
ded_COUNT.grid(row = 1, column = 2, pady = 1, padx = 1)

app_name = Label(foot_frame, text= "LAST UPDATED {}".format(time.strftime("%A  %d%B%Y  %I:%M %p ")), width = 150, height  = 1, pady = 5,padx = 0, relief = "flat", anchor = CENTER, font = ("arial 10"), bg = col3, fg = col2)
app_name.pack()



def re():pass

#########################################################################################3
fig = Figure(figsize=(7, 2), dpi=100)
fig.add_subplot(111).plot(x, y)

canvas = FigureCanvasTkAgg(fig, master=app)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().place(x = 100, y = 220)





b1 = Button(app,text="REFRESH", width=120,height=3 , bg = col4, fg = col1, command = app.update  ,font = ('newspaper', 10))
b1.place(x = 70, y = 500)

b2 = Button(app, text = "EXIT",fg = 'white', bg = 'orange'  , width=120,height=1 ,font = ('newspaper', 10, "bold"), command = app.destroy )
b2.place(x = 70, y = 580)


app.mainloop()
