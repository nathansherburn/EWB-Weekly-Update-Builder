#!/user/bin/python

from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename, asksaveasfilename

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import ttk


# create a window
main_window = Tk()
main_window.wm_title("Weekly Update Maker")
#main_window.geometry('800x600')

# define functions for text parsing
def add_update():
	if collie_cup.get() == 1:
		output_text.insert(INSERT, "<div style='background-color: #3D9599; padding: 10px; color: #fff;'>\n\n")
		output_text.insert(INSERT, "<h1 style='font-weight: normal;'>This week's Collie Cup goes to<h1>\n\n")
		output_text.insert(INSERT, "<img src='http://www.psdgraphics.com/file/gold-trophy-cup.jpg' alt='trophy' style='width: 100%;' />\n\n")
	else:
		output_text.insert(INSERT, "<div style='background-color: #e9e9e9; padding: 10px; color: #777;'>\n\n")
		
	output_text.insert(INSERT, "<h1>"+staff_entry.get()+"</h1>\n")
	output_text.insert(INSERT, "<h2>Last Week</h2>\n")
	output_text.insert(INSERT, "<ul>\n")

	line = "1"
	for line in range( 1, int(last_week_text.index("end-1c")[0])+1 ): # grab the index of last character as a string and the access element 0
		output_text.insert(INSERT, "\t<li>"+last_week_text.get(str(line)+".0", str(line)+".end")+"</li>\n")

	output_text.insert(INSERT, "</ul>\n")
	output_text.insert(INSERT, "<h2>This Week</h2>\n")
	output_text.insert(INSERT, "<ul>\n")

	line = "1"
	for line in range( 1, int(this_week_text.index("end-1c")[0])+1 ): # grab the index of last character as a string and the access element 0
		output_text.insert(INSERT, "\t<li>"+this_week_text.get(str(line)+".0", str(line)+".end")+"</li>\n")

	output_text.insert(INSERT, "</ul>\n")

	output_text.insert(INSERT, "</div>\n\n")


def add_text():
	output_text.tag_add("text", INSERT)
	output_text.tag_config("text", background="medium spring green", foreground="black")
	output_text.insert(INSERT, "<div style='background-color: #009F4C; padding: 10px; color: #fff; text-align: center;'>\n")
	output_text.insert(INSERT, "<p>"+add_text_entry.get()+"</p>\n")
	output_text.insert(INSERT, "</div>\n\n")



def add_image():
	output_text.tag_add("image", "linestart", "lineend")
	output_text.insert(INSERT, "<div style='background-color: #009F4C; padding: 10px; color: #fff;'>\n")
	output_text.insert(INSERT, "\t<img src='"+add_image_entry.get()+"' style='width: 100%;' />\n")
	output_text.insert(INSERT, "</div>\n\n")
	output_text.tag_config("image", background="medium spring green", foreground="black")




# NAME frame
name_frame = Frame(main_window)
name_frame.grid(row=1, column=1, sticky=W)

staff_label = Label(name_frame, text='Name: ')
staff_label.grid(row=1, column=1)

staff_entry = Entry(name_frame)
staff_entry.grid(row=1, column=2)

# LAST WEEK frame
last_week_frame = Frame(main_window)
last_week_frame.grid(row=2, column=1)

last_week_label = Label(last_week_frame, text='Last week: ')
last_week_label.grid(row=1, column=1, sticky=W)

last_week_text = Text(last_week_frame, height=10, wrap=WORD)
last_week_text.insert(INSERT, "")
last_week_text.grid(row=2, column=1)

# THIS WEEK frame
this_week_frame = Frame(main_window)
this_week_frame.grid(row=3, column=1)

this_week_label = Label(this_week_frame, text='This week: ')
this_week_label.grid(row=1, column=1, sticky=W)

this_week_text = Text(this_week_frame, height=10, wrap=WORD)
this_week_text.insert(INSERT, "")
this_week_text.grid(row=2, column=1)

# ADD frame
add_frame = Frame(main_window)
add_frame.grid(row=4, column=1, sticky=E)

collie_cup = IntVar()
collie_cup_checkbox = Checkbutton(add_frame, text="Collie Cup", variable=collie_cup)
collie_cup_checkbox.grid(row=1, column=1)

add_update_btn = Button(add_frame, text='Add Update to HTML', width=20, command=add_update)
add_update_btn.grid(row=1, column=2)

add_text_entry = Entry(add_frame)
add_text_entry.grid(row=2, column=1)

add_text_btn = Button(add_frame, text='Add Text to HTML', width=20, command=add_text)
add_text_btn.grid(row=2, column=2, sticky=E)

add_image_entry = Entry(add_frame)
add_image_entry.grid(row=3, column=1)

add_image_btn = Button(add_frame, text='Add Image to HTML', width=20, command=add_image)
add_image_btn.grid(row=3, column=2, sticky=E)


# OUTPUT frame
output_text_frame = Frame(main_window)
output_text_frame.grid(row=1, column=2, rowspan=4)

output_text_label = Label(output_text_frame, text='HTML: ')
output_text_label.grid(row=1, column=1, sticky=W)

output_text = Text(output_text_frame)
output_text.insert(END,"""
<meta charset="utf-8" />
<div style="max-width: 600px; margin: 0 auto; background-color: #efefef; font-family: sans serif;">
<div style="background-color: #009F4C; font-size: 3em; color: #fff; padding: 10px;">
<br>
Weekly Staff Update!
<br>
</div>
<div  style="color: #4b4b4b;">



<div style="background-color: #009F4C; color: #fff; padding: 10px; text-align: center;">
<i>Enjoy the week!</i>
</div>
</div>
</div>
""")
output_text.grid(row=2, column=1)

output_text.tag_add("boilerplate", "1.0", "10.0")
output_text.tag_add("boilerplate", "13.0", END)
output_text.tag_config("boilerplate", background="dark slate gray", foreground="gray")

main_window.mainloop()



# http://imgur.com/P68F1gy