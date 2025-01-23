import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from utils import spaceclaim_transformation


class MainGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Foil Transformation Tool')
        self.window.geometry('450x300')

        # Variables
        self.file_path = tk.StringVar(value="File location") #Location of original file from Airfoil Tools
        self.directory_path = tk.StringVar(value="Output directory") #Location of diretory in which modified airfoil will be saved
        self.foil_name = tk.StringVar(value="New_airfoil") #Name of transformed airfoil
        self.status = tk.StringVar(value="No airfoil has been transformed") #Status of action

        self.spaceclaim_option = tk.BooleanVar(value=False) #Option if Spaceclaim format will be outputed
        self.xfoil_xflr_option = tk.BooleanVar(value=False) #Option if Xfoil xflr5 format will be outputed
        self.creo_option = tk.BooleanVar(value=False) #Option if Creo format will be outputed
        

        #Build GUI

        self.create_widgets()

    def create_widgets(self):
        #title in widget
        self.Top_label = ttk.Label(master=self.window, 
                                   text="Airfoil to be transformed")
        self.Top_label.pack()

        # Entry for original file location
        self.entry_file_path = ttk.Entry(master=self.window,
                                         textvariable=self.file_path,
                                         width=40
                                         )
        self.entry_file_path.pack()

        self.button_file_path = ttk.Button(master=self.window,
                                           text="Get file",
                                           command= self.get_filepath)
        self.button_file_path.pack()

        self.check_spaceclaim = ttk.Checkbutton(master=self.window,
                                                text="SpaceClaim",
                                                command=self.transform_status,
                                                variable=self.spaceclaim_option,
                                                onvalue=True,
                                                offvalue=False
                                                )
        self.check_spaceclaim.pack()

        self.check_xfoil_xflr = ttk.Checkbutton(master=self.window,
                                                text="Xfoil/Xflr5",
                                                command=self.transform_status,
                                                variable=self.xfoil_xflr_option,
                                                onvalue=True,
                                                offvalue=False
                                                )
        self.check_xfoil_xflr.pack()

        self.check_creo= ttk.Checkbutton(master=self.window,
                                                text="Creo",
                                                command=self.transform_status,
                                                variable=self.creo_option,
                                                onvalue=True,
                                                offvalue=False
                                                )
        self.check_creo.pack()
        
        self.entry_dir_path = ttk.Entry(master=self.window,
                                        textvariable=self.directory_path,
                                        width='40')
        self.entry_dir_path.pack()

        self.button_dir_path = ttk.Button(master=self.window,
                                          text="Select directory",
                                          command=self.get_dirpath
                                          )
        self.button_dir_path.pack()

        self.entry_foil_name = ttk.Entry(master=self.window,
                                         textvariable=self.foil_name)
        self.entry_foil_name.pack()

        self.button_transform = ttk.Button(master=self.window,
                                           text = 'Transform',
                                           state=tk.DISABLED,
                                           command= self.transform_button
                                           )
        self.button_transform.pack()

        self.status_label = tk.Label(text=self.status.get())
        self.status_label.pack()    


        self.button_exit = ttk.Button(master=self.window,
                                      text='Neplecha ukončena',
                                      command=self.window.quit
                                      )
        self.button_exit.pack()

    def run(self):
        self.window.mainloop()


    def get_filepath(self):
        self.filetypes = (('CSV','*.csv'), ('All files', '*.*'))
        self.f = fd.askopenfile(filetypes=self.filetypes)
        self.file_path.set(self.f.name.replace('/','\\'))

    def get_dirpath(self):
        d = fd.askdirectory()
        d=d.replace('/','\\')
        d=d+'\\'
        self.directory_path.set(d)

    def transform_button(self):
        result = spaceclaim_transformation(self.file_path.get(),self.directory_path.get(),self.foil_name.get())
        print(result)
        if result == "succes":
            print('Airfoil transformed sucessfully. GUI')
            self.status_label.config(text="Airfoil has been transformed")



    def transform_status(self):
        print('SpaceClaim output status:'+ str(self.spaceclaim_option.get()))
        print('xfoil/xflr5 output status:'+ str(self.xfoil_xflr_option.get()))
        print('Creo output status:'+ str(self.creo_option.get()))
        
        if self.spaceclaim_option.get() == True:
            self.button_transform.config(state=tk.NORMAL)
        elif self.xfoil_xflr_option.get() == True:
            self.button_transform.config(state=tk.NORMAL)
        elif self.creo_option.get() == True:
            self.button_transform.config(state=tk.NORMAL)
        else:
            self.button_transform.config(state=tk.DISABLED)

    
