import tkinter as tk
from tkinter import filedialog
from TSRemove import TSRemove
import sys

root = tk.Tk()
instructionalInfo = """
Hi! To begin, Use the 'Select Folder' button to choose the folder holding
the products to discontinue.
"""


howTo = tk.Label(root, padx = 10,
                 text=instructionalInfo,
                 justify="left").pack(fill=tk.X, side=tk.TOP)

root_menu = tk.Menu(root)
root.config(menu = root_menu)

def folderSelect():
    file_path = filedialog.askdirectory()

def exit_prog():
    sys.exit()


file_menu = tk.Menu(root_menu)
root_menu.add_command(label = "Exit", command=exit_prog)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.BOTTOM)

select_button = tk.Button(button_frame, text='Select Folder', command=folderSelect)
run_button = tk.Button(button_frame, text='Run', command=TSRemove)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

select_button.grid(row=0, column=0, sticky=tk.W+tk.E)
run_button.grid(row=0, column=1, sticky=tk.W+tk.E)

root.mainloop()
