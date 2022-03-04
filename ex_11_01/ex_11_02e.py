import re
fname = input("Enter a File: ")
fhand = open(fname)
lst = []


for lines in fhand:
    line = lines.rstrip()
    num = re.findall('^New\sRevision:\s.([0-9.]+)', line)
    if len(num) > 0:
        num = int(num)
        #lst.append(num)
        print(num)
            
    
    #for num:
        #num = float(num)
        #lst.append(num)
        
#lst_count= len(lst)
#total = sum(lst)
#print(total)
        



        
