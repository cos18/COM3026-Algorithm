import csv

j=[]

f = open('./j.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    j.append(line[0])
f.close() 
print(j)   