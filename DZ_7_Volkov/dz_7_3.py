import os, shutil

directory = r'my_project\templates'
for root, dirs, files in os.walk('my_project'):
    if root == directory:
        break
    for file in files:
        if file.rsplit('.',1)[-1].lower() == 'html':
            os.makedirs(os.path.join(directory,root.split('\\')[-1]), exist_ok=True)
            shutil.copyfile(os.path.join(root,file), os.path.join(directory, os.path.join(root.split('\\')[-1], file)))