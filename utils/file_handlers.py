import pandas as pd



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

