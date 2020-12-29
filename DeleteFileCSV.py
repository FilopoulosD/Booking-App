import os

def delete(file):
    if os.path.exists(file):
        os.remove(file)

