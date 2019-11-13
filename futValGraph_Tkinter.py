from tkinter import *

window = Tk(className="window", )

window.title("Investment Growth Chart")
window.minsize(width=360, height=280)

# label = tkinter.Label(window, text="Hello World!").pack()

win = Canvas(window, width=320, height=240, bg='white')
win.place(relx=0.5, rely=0.5, anchor=CENTER)
# win.pack(anchor='center')
principal = 2500
apr = 0.1

label_y = 220
label_x = 20
label_values = 0

year = 0
year_y = 235
year_x = 50

bar_width = 25
bar_height_constant = 100 / 5000
rectangle_bottom_x = 40
rectangle_bottom_y = 220
rectangle_top_x = 40 + bar_width
rectangle_top_y = rectangle_bottom_y - principal * bar_height_constant

for i in range(5):
    win.create_text(label_x, label_y, text='{0}K'.format(label_values))

    label_values += 2.5
    label_y -= 50

for years in range(11):
    win.create_text(year_x, year_y, text='Y{0}'.format(years))

    year_x += 25

for j in range(11):
    win.create_rectangle(rectangle_bottom_x, rectangle_bottom_y,
        rectangle_top_x, rectangle_top_y, fill='green')

    principal = principal * (1 + apr)
    rectangle_bottom_x = rectangle_top_x
    rectangle_top_x += bar_width
    rectangle_top_y = rectangle_bottom_y - principal * bar_height_constant

window.mainloop()
