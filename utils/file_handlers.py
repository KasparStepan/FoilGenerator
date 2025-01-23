import pandas as pd


class File_handler:

    def __init__(self, 
                 file_path_input: str = "",
                 airfoil_name: str = "Edited_Airfoil",
                 directory_path: str = "",
                 output_option: list = [False,False,False]):
        
        
        if not isinstance(file_path_input, str):
            raise TypeError("file_path_input must be a string.")
        if not isinstance(airfoil_name, str):
            raise TypeError("airfoil_name must be a string.")
        if not isinstance(directory_path, str):
            raise TypeError("directory_path must be a string.")
        
        self.output_setup = {'SpaceClaim': [output_option[0], '_spaceclaim',self.spaceclaim_output],
                             'Xfoil/xflr5': [output_option[1], '_xfoil_xflr',self.xfoil_output],
                             'PTC Creo': [output_option[2], '_Creo',self.creo_output],
                             }
        
        self.text_to_remove = 'Camber line'
        self.data = pd.DataFrame()
        self.modified_file = pd.DataFrame()
        self.original_file = pd.DataFrame()
        self.file_path_input = file_path_input
        self.airfoil_name = airfoil_name
        self.directory_path = directory_path

        self.spaceclaim_output_airfoil = pd.DataFrame()
        self.creo_ouptut_airfoil = pd.DataFrame()
        self.xfoil_xflr_ouptut_airfoil = pd.DataFrame()

        self.data_load()

    def data_load(self):
        self.original_file = pd.read_csv(self.file_path_input, delimiter=',')
        
        
        self.modified_file = self.original_file.head(-5).tail(-8)
        self.modified_file = self.modified_file.reset_index(drop=True)
        self.modified_file.columns.values[0] = 'X_coordinate'
        self.modified_file.columns.values[1] = 'Y_coordinate'

        index_to_remove = self.modified_file[self.modified_file['X_coordinate'] == self.text_to_remove].index[0]

        self.data = self.modified_file.iloc[:(index_to_remove-1)]\
        
    def save_airfoil(self):
         for key, value in self.output_setup.items():
             print(f"Output for {key} has started")
             if value[0] == True:
                 value[2]
             print(f"Output for {key} has finished")
                 
         
         pass
    
    def spaceclaim_output(self):
        self.spaceclaim_output_airfoil['Column_1'] = [1]*self.data.shape[0]
        self.spaceclaim_output_airfoil['X'] = self.data.X_coordinate
        self.spaceclaim_output_airfoil['Y'] = self.data.Y_coordinate
        new_row = {'Column_1':'Polyline=true', 'X': '', 'Y':''}

        self.spaceclaim_output_airfoil = pd.concat([pd.DataFrame([new_row]),self.spaceclaim_output_airfoil],ignore_index=True)

        self.spaceclaim_output_airfoil.to_csv(self.directory_path+self.airfoil_name+self.output_setup['SpaceClaim'][1]+'.txt', sep='\t', index=False,header=False)


    def xfoil_output(self):
        pass

    def creo_output(self):
        pass


test = File_handler(file_path_input='C:\\Users\\kaspa\\OneDrive - VUT\\01_PhD\\00_vyuka\\OCF\\Airfoils\\e423-il.csv')

print(test.data)


'''



def data_load(filepath_input):
    original_file = pd.read_csv(filepath_input, delimiter=',')

    text_to_remove = 'Camber line'

    modified_file = original_file.head(-5).tail(-8)
    modified_file = modified_file.reset_index(drop=True)
    modified_file.columns.values[0] = 'X_coordinate'
    modified_file.columns.values[1] = 'Y_coordinate'

    return modified_file



def output_data(dataFrame, directory_output, airfoil_name, output_format):

    for i in 

    dataFrame.to_csv(directory_output+airfoil_name+'.txt', sep='\t', index=False,header=False)
    print('Airfoil transformed sucessfully-filehandler.')
    return "succes"




def spaceclaim_transformation(filepath_input,directory_output,airfoil_name):
    original_file = pd.read_csv(filepath_input, delimiter=',')

    text_to_remove = 'Camber line'

    modified_file = original_file.head(-5).tail(-8)
    modified_file = modified_file.reset_index(drop=True)
    modified_file.columns.values[0] = 'X_coordinate'
    modified_file.columns.values[1] = 'Y_coordinate'

    data = pd.DataFrame()
    data['Column_1'] = [1]*modified_file.shape[0]
    data['X'] = modified_file.X_coordinate
    data['Y'] = modified_file.Y_coordinate
    new_row = {'Column_1':'Polyline=true', 'X': '', 'Y':''}

    data = pd.concat([pd.DataFrame([new_row]),data],ignore_index=True)

    index_to_remove = data[data['X'] == text_to_remove].index[0]

    data = data.iloc[:(index_to_remove-1)]

    data.to_csv(directory_output+airfoil_name+'.txt', sep='\t', index=False,header=False)
    print('Airfoil transformed sucessfully-filehandler.')
    return "succes"
'''
