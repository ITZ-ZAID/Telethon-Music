import os 
files = [] 
  
for files in os.listdir("./Zaid/helper/thumb"): 
     if files.endswith("PNG"): 
         files.append(files[:-4])
