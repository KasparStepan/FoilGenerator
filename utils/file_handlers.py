import pandas as pd

file_path = "C:/Users/kaspa/OneDrive - VUT/01_PhD/00_vyuka/OCF/Airfoils/e423-il.csv"

original_file = pd.read_csv(file_path, delimiter=',')

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

data.to_csv('output.txt', sep='\t', index=False,header=False)




