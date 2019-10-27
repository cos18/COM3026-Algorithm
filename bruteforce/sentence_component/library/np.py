import csv

np=[]

f = open(r'np.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    np.append(line[0])
f.close() 
print(np)   