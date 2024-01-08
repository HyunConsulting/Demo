
# create the initial window to display
def create_main_window():

	# create a window for main form of app
	woda_form = tkinter.Tk()

	# title for dialog box
	woda_form.title("WODA (Wise Owl Dating Agency)")

	# set form width and height
	form_width = 400
	form_height = 200

	# get screen width and height
	screen_width = woda_form.winfo_screenwidth()
	screen_height = woda_form.winfo_screenheight()

	# calculate horizontal and vertical offset
	horizontal_offset = \
		int((screen_width/2) - (form_width/2))
	vertical_offset = \
		int((screen_height/2) - (form_height/2))

	# show form in middle of screen
	woda_form.geometry('{0}x{1}+{2}+{3}'
	.format(form_width,
	form_height,horizontal_offset,vertical_offset))

	# stop the window being resizable
	woda_form.resizable(False,False)

	return woda_form

# use the TKinter GUI module
import tkinter

# this module doesn't automatically 
# get imported - we'll use it do display
# message boxes
import tkinter.messagebox

# call function to create form to be displayed
woda_form = create_main_window()

# the event-handler for the OK button
def ok_clicked():

	# get what was typed in to widget
	this_person_name = person_name.get()
	
	# get what was typed into multiline text
	# widget (start at row 1, character 0 - 
	# ie the start - and go on to the end, 
	# missing out the final new line character)
	this_person_about = person_about.get(
		"1.0",tkinter.END)
	print(this_person_about)

	# display a suitable message
	tkinter.messagebox.showinfo("Welcome",
	"Welcome " + this_person_name + 
	"\n\n" + this_person_about
	)

# event-handler for cancel button
def cancel_clicked(event):
	
	# close the form
	woda_form.quit()

# add name label and textbox
lbl_name = tkinter.Label(woda_form, 
text="Your name:")
lbl_name.place(x=20,y=20)

person_name = tkinter.Entry(woda_form)
person_name.place(x=120,y=20)

# add info about self
lbl_about = tkinter.Label(
	woda_form, text="About yourself:")
lbl_about.place(x=20,y=50)

# add a text widget 
person_about = tkinter.Text(
	woda_form,foreground="darkred")
person_about.place(x=120,y=50,
height=100, width=250)

# set the background colour using property
person_about["bg"] = "#ffeeff"

# set the cursor using configuration
person_about.configure(cursor = "spider")

# add an OK button to the window (and attach 
# event-handler for when it's clicked)
btn_add = tkinter.Button(
	woda_form,
	text="OK",
	command=ok_clicked)
btn_add["padx"] = 5
btn_add["pady"] = 5
btn_add.place(x=120, y=160)

# add CANCEL button to this frame
btn_cancel = tkinter.Button(
	woda_form,text="Cancel")
btn_cancel["padx"] = 5
btn_cancel["pady"] = 5

# invoke cancel when user presses ENTER or 
# clicks on left-hand mouse button
btn_cancel.bind('<Return>', cancel_clicked)
btn_cancel.bind('<Button-1>', cancel_clicked)

btn_cancel.place(x=180, y=160)

# display the form
woda_form.mainloop()

