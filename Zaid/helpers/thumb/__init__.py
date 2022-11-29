import os 
files = [] 
  
for pussy in os.listdir("./Zaid/helper/thumb"): 
     if pussy.endswith("PNG"): 
         files.append(pussy[:-4])
