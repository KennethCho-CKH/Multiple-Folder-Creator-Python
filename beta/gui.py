import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import os, shutil, errno
from aifc import Error
 
value = 1
def btnpressed():
       global value
       value -= 1
       if value == 0:
              fd.askopenfilename()
              value = 1
       else:
              pass 
 
root = tk.Tk()
 
root.title("Multiple Folder Creator")
 
root.geometry("500x250")
 
program_title_gui = tk.Label(root, text = "Multiple Folder Creator")
program_title_gui.config(font =("Helvetica", 14))
 
path_text_gui = tk.Label(root, text = "Type where you want your folders to be created: ")
path_text_gui.config(font =("Helvetica", 10))
 
path_input_gui = tk.Text(root, height = 1, width = 50)
path = path_input_gui.get("1.0",'end-1c')
folderpath = path_input_gui
 
name_text_gui = tk.Label(root, text = "Type the filename you desired (use space to separate): ")
name_text_gui.config(font =("Helvetica", 10))
 
name_input_gui = tk.Text(root, height = 5, width = 50)
name = name_input_gui.get("1.0",'end-1c')
filename = name_input_gui

def create_folder():
    os.makedirs(r'C:\Users\persk\Documents\Sandbox\test\\')
    #shutil.move("C:\\" + filename, folderpath)

broswe_file_btn = ttk.Button(root, text = "Broswe Files", command = btnpressed)
#broswe_file_btn.grid(row = 20, column = 1)
 
create_btn = ttk.Button(root, text = "Create", command = create_folder)
#create_btn.grid(row = 20, column = 2)
 
exit_btn = ttk.Button(root, text = "Exit", command = root.destroy) 
#exit_btn.grid(row = 20, column = 3)
 
program_title_gui.pack()
path_text_gui.pack()
path_input_gui.pack()
name_text_gui.pack()
name_input_gui.pack()
broswe_file_btn.pack()
create_btn.pack()
exit_btn.pack()
 
tk.mainloop()