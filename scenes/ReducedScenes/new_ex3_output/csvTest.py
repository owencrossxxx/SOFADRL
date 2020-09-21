# importing library 
import csv 
  
# opening the csv file in 'w' mode 
file = open('g4g.csv', 'wb') 
  
with file as f: 
    # identifying header   
    #header = ['Organization', 'Established'] 
    #writer = csv.DictWriter(file, fieldnames = header) 
    writer = csv.writer(f)
    a = [1,2,3,4]
    b = [6, 6 ,5,9]
    c = [a,b]
    # writing data row-wise into the csv file 
    #writer.writeheader() 
    writer.writerows(c)
        #writer.writerow(b[i])