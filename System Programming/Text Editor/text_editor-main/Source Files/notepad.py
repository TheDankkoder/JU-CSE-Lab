from tkinter import *
from tkinter import filedialog
from tkinter import font
  
root = Tk()
root.geometry("750x500")
root.title("NotePad")


#Create New File function

def new_file():
    my_text.delete("1.0", END)
    root.title('New File - Textpad')
    status_bar.config(text= "New File    ")
#create main frame

my_frame = Frame(root)
my_frame.pack(pady = 5)


#create scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill= Y)
#create text box

my_text = Text(my_frame,width = 150 , height= 95 , font = ("Helvetica",16), selectbackground="yellow", selectforeground="black", undo= True, yscrollcommand= text_scroll.set)
my_text.pack()

#Configure scrollbar

text_scroll.config(command= my_text.yview)


#Create Menu

my_menu = Menu(root)
root.config(menu = my_menu)

#Add File Menu


file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label="New", command= new_file)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit" , command=root.quit)

#Add Edit Menu

edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#Add Status Bar
status_bar = Label(root, text='Ready   ', anchor=E)
status_bar.pack(fill=X,side=BOTTOM, ipady=5)

root.mainloop()