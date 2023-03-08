from tkinter import *

window = Tk()
window.geometry('500x200')
window.title('GUI')
label = Label(window, text='Python Tkinter')
label.pack(expand=1)
frame = Frame(window, relief='ridge', borderwidth=20)
frame.pack(fill='both', expand=1)
window.mainloop()
