import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

def get_filepath(string_var):
    filetypes = (('Text files','*.txt'), ('All files', '*.*'))

    f = fd.askopenfile(filetypes=filetypes)

    string_var.set(f.name)




def main_page_gui():

    # Main window of Foil Tranformation Tool

    window = tk.Tk()
    window.title('Foil Transformation Tool')
    window.geometry('400x200')

    string_var = tk.StringVar(value='File loaction')
    spaceclaim_var = tk.BooleanVar(value=False)

    label = ttk.Label(master=window, 
                      text='File to be transformed')
    label.pack()

    entry_file_path = ttk.Entry(master=window,
                                textvariable=string_var,
                                width='40')
    entry_file_path.pack()

    button = ttk.Button(master=window, 
                        text="Get file", 
                        command=lambda: get_filepath(string_var))
    button.pack()

    check_spaceclaim = ttk.Checkbutton(master=window,
                                       text='SpaceClaim',
                                       command= lambda: print('SpaceClaim output status:'+ str(spaceclaim_var.get())),
                                       variable=spaceclaim_var,
                                       onvalue=True,
                                       offvalue=False,
                                       )
    check_spaceclaim.pack()



    



    window.mainloop()


