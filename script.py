import os
import bpy
import sys



os.chdir(os.path.dirname(bpy.path.abspath("//")))



ans = []
 

with open("data/noname-1665346695947.tsv") as f:
   
  # Read data line by line
  for line in f:
     
    # split data by tab
    # store it in list
    l=line.split('\t')
     
    ans.append((float(l[2].replace(',','.')), float(l[3].replace(',','.')), float(l[4].replace(',','.'))))
print(ans)

obj = bpy.context.object

for i,a in enumerate(ans):
    obj.location[2] = a[2]
    obj.keyframe_insert(data_path="location", frame=i*10, index=2)
