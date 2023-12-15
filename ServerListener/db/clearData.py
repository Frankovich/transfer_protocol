import os
 
dir = './images'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = './coordinates'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))