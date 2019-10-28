def check(f, s, ct):
    if f==s:
        ct[f]+=1
        return
    m = (f+s)//2
    check(f, m, ct)
    check(m+1, s, ct)

person = int(input("몇 명인가요? "))
timetable = []
for i in range(person):
    tmptt = []
    while True:
        line = input("").split()
        if(line[0]=="."):
            break
        for j in range(1, len(line)):
            time = line[j]
            start = int(line[j][:4])
            end = int(line[j][5:])
            line[j] = [(start//100-9)*12+start%100//5, (end//100-9)*12+end%100//5]
        tmptt.append(line)
    timetable.append(tmptt)

day = ["MON", "TUE", "WED", "THU", "FRI"]
for d in day:
    gonggang = []
    checktime = [0]*145
    for p in timetable:
        for dtt in p:
            if dtt[0]==d:
                for tt in dtt[1:]:
                    check(tt[0], tt[1], checktime)
    start = -1
    for t in range(145):
        if start==-1 and checktime[t]==0:
            start = (0 if (t==0) else (t-1))
        if start != -1 and checktime[t]>0:
            if t-start>=6:
                gonggang.append([start, t])
            start = -1
    if start!=-1 and 144-start>=6:
        gonggang.append([start, 144])
    if len(gonggang)>0:
        print(d, end=' ')
        for g in gonggang:
            print("{:0>2}{:0>2}-{:0>2}{:0>2}".format(g[0]//12+9, g[0]%12*5, g[1]//12+9, g[1]%12*5), end=' ')
        print()