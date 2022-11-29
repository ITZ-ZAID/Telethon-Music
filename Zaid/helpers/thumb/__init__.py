import os 
files = [] 
  
for pussy in os.listdir("./assets"): 
     if pussy.endswith("PNG"): 
         files.append(pussy[:-4])
