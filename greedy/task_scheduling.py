class Sceduler:
    def __init__(self):
        self.tasks = []
        
        print("작업의 시작 시간과 끝 시간을 입력해주세요.")
        print("예) 10 20")
        print("0 0을 입력하면 작업 입력이 종료됩니다.")

        while True:
            s, e = map(int, input(' => ').split())
            if s==e and e==0:
                break
            if s>=e:
                print("시작시간보다 끝나는 시간이 빠르거나 같을 수 없습니다.")
                continue
            self.tasks.append([s, e])

        self.tasks.sort()

    def assign(self):
        self.process=[]
        for t in self.tasks:
            locate=0
            while locate<len(self.process):
                if self.process[locate][-1][1]<=t[0]:
                    self.process[locate].append(t)
                    break
                locate+=1
            if locate == len(self.process):
                self.process.append([t])
    
    def status(self):
        for i in range(len(self.process)):
            print("{}번 프로세서 : {}".format(i+1, self.process[i]))

my_sceduler = Sceduler()
my_sceduler.assign()
my_sceduler.status()