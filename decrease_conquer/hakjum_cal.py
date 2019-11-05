import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

class Graduate:
    def __init__(self):
        global BASE_DIR
        self.gyojic=[]
        self.major=[]
        with open(os.path.join(BASE_DIR, 'gyoil.txt'), 'r') as f:
            gyoil = list(map(lambda n:n[:-1], f.readlines()))
            self.gyojic.append(gyoil)
        with open(os.path.join(BASE_DIR, 'gyopil.txt'), 'r') as f:
            gyopil = list(map(lambda n:n[:-1], f.readlines()))
            self.gyojic.append(gyopil)
        self.gyo_unit = 22
        self.gyo_nowunit = (len(self.gyojic[0])+len(self.gyojic[1])-2)*2

        while True:
            print("단일/복수전공 여부를 입력해주세요")
            print("1은 단일전공, 2는 복수전공입니다.")
            select = input(">> ")
            if select=="1" or select=="2":
                self.major_unit = (66 if select=="1" else 50)
                break
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")

        while True:
            print("학번을 입력해주세요.")
            print("예를 들어, 18학번은 18을 입력해주세요.")
            try:
                self.hakbun = int(input(">> "))
                self.txt = (['jeonil_old.txt', 'jeonpil_old.txt'] if self.hakbun<17 else ['jeonil_new.txt', 'jeonpil_new.txt'])
                for t in self.txt:
                    with open(os.path.join(BASE_DIR, t), 'r') as f:
                        tmp = list(map(lambda n:n[:-1], f.readlines()))
                        self.major.append(tmp)
                check = self.major[0]+self.major[1]
                self.major_nowunit = self.major_unit - (32-len(check))*3 + (0 if "상업정보교과논리논술" in check else 1)
                break
            except ValueError:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                
    def status(self):
        print("="*15)
        print("남은 학점")
        print("   전공 {}/{}".format(self.major_nowunit, self.major_unit))
        print("   교직 {}/{}\n".format(self.gyo_nowunit, self.gyo_unit))
        print("남은 전공필수 과목")
        for lesson in self.major[1]:
            print("   {}".format(lesson))
        print("남은 교직필수 과목")
        for lesson in self.gyojic[1]:
            print("   {}".format(lesson))
        print("="*15)
        
    def listen_lesson(self, lesson):
        for g in self.gyojic:
            if lesson in g:
                g.remove(lesson)
                self.gyo_nowunit -= 2
                if self.gyo_nowunit<0:
                    self.gyo_nowunit = 0
                self.save_gyo()
                return True
        for m in self.major:
            if lesson in m:
                m.remove(lesson)
                self.major_nowunit -= 3
                if lesson == "상업정보교과논리논술":
                    self.major_nowunit += 1
                if self.major_nowunit<0:
                    self.major_nowunit=0
                self.save_major()
                return True
        return False
    
    def save_gyo(self):
        os.remove(os.path.join(BASE_DIR, 'gyoil.txt'))
        os.remove(os.path.join(BASE_DIR, 'gyopil.txt'))
        with open(os.path.join(BASE_DIR, 'gyoil.txt'), 'w') as f:
            f.writelines(list(map(lambda n:n+'\n', self.gyojic[0])))
        with open(os.path.join(BASE_DIR, 'gyopil.txt'), 'w') as f:
            f.writelines(list(map(lambda n:n+'\n', self.gyojic[1])))
            
    def save_major(self):
        for i in range(2):
            os.remove(os.path.join(BASE_DIR, self.txt[i]))
            with open(os.path.join(BASE_DIR, self.txt[i]), 'w') as f:
                f.writelines(list(map(lambda n:n+'\n', self.major[i])))
            
    def is_graduate(self):
        return self.gyo_nowunit<=0 and self.major_nowunit<=0 and not self.major[1] and not self.gyojic[1]
                    
# 본 프로그램 부분

now = Graduate()
now.status()
while True:
    cmd = input(" >> ")
    if cmd=='status' or now.listen_lesson(cmd):
        now.status()
        if now.is_graduate():
            print("졸업!!!")
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("입력 가능한 문자열은 문제 조건을 확인해주세요.")
        