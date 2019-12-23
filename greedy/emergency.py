import heapq
# GUI를 구현하는데 너무 어려워 일단 CUI로 구현했습니다.
# 우선순위 큐를 사용해 구현했습니다.

class Patient:
    timepoint = 0
    def __init__(self, pid, time, point):
        self.pid = pid
        self.time = time
        self.point = point


class Hospital:
    plist = []
    time = 0

    def person_in(self):
        pid = int(input("환자 번호를 입력해주세요 : "))
        point = int(input("응급정도를 입력해주세요 : "))
        
        p_in = Patient(pid, point, self.time)
        heapq.heappush(self.plist, (-point, p_in))

    def update_time(self):
        while True:
            time = input("시간을 입력해주세요 (형식 - 시:분 - 12:34) : ")
            try:
                time = int(time[:2])*60 + int(time[3:])
            except:
                print("입력 형식이 잘못되었습니다.")
            if type(time) is int:
                if self.time > time:
                    print("현재 시간보다 이른 시간으로 시간을 업데이트 할 수 없습니다.")
                else:
                    break
        self.time = time

        for p in range(len(self.plist)):
            self.plist[p][1].timepoint = (self.time-self.plist[p][1].time)//20

        newplist = []
        for p in range(len(self.plist)):
            heapq.heappush(newplist, (-self.plist[p][1].timepoint-self.plist[p][1].point, self.plist[p][1]))
        
        self.plist = newplist

    def person_out(self):
        out = heapq.heappop(self.plist)
        print("현재 진료하셔야 할 환자는 {}번 환자 입니다.".format(out[1].pid))

    def status(self):
        print("대기 큐 : ", end="")
        for p in self.plist:
            print(p[1].pid, "", end="")

hos = Hospital()

while True:
    print("\n===MENU===")
    print("1. 환자 도착")
    print("2. 진료 가능")
    print("3. 대기 확인")
    print("4. 시간 변경")
    print("현제시간 - {:0>2}:{:0>2}".format(hos.time//60, hos.time%60))
    choice = input("=>")
    try:
        choice = int(choice)
    except:
        print("올바른 형식의 입력이 아닙니다")

    if type(choice) is int:
        if choice==1:
            hos.person_in()
        elif choice==2:
            hos.person_out()
        elif choice==3:
            hos.status()
        elif choice==4:
            hos.update_time()
        else:
            print("올바른 형식의 입력이 아닙니다")
    

