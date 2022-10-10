
ans = []
 
# open .tsv file
with open("data/noname-1665346695947.tsv") as f:
   
  # Read data line by line
  for line in f:
     
    # split data by tab
    # store it in list
    l=line.split('\t')
     
    ans.append((float(l[2].replace(',','.')), float(l[3].replace(',','.')), float(l[4].replace(',','.'))))
 

print(ans)
