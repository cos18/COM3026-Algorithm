import csv

nr=[]

f = open(r'C:\Users\JUNGMIN LEE\OneDrive\Desktop\github\COM3026-Algorithm\bruteforce\sentence_component\library\nr.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    nr.append(line[0])
f.close() 
print(nr)   