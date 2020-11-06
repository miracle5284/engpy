import os

def get_root(D):
    return os.path.basename(D)
    
base = os.getcwd()
while True:
    path_  = os.path.basename(base)
    if path_ == 'engpy':
        break
    base = base[:-len(path_)-1]
    if not base:
        break
