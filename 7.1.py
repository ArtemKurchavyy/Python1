import os

subfolder_names = ['settings', 'mainapp', 'adminapp', 'authapp']
folder_name = 'my_project'
if not os.path.exists(folder_name):
    new_dir = [os.makedirs(os.path.join(folder_name, subfolder_name)) for subfolder_name in subfolder_names
               if not os.path.exists(subfolder_name)]
else:
    folder_name = f'{folder_name}_new'
    if not os.path.exists(folder_name):
        new_dir = [os.makedirs(os.path.join(folder_name, subfolder_name)) for subfolder_name in subfolder_names
                   if not os.path.exists(subfolder_name)]
    else:
        print('Папка с таким именем есть. Езмените название.')
