import sys

class Change:
    def __init__(self):
        self.money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        self.money_left = [0]*8

        self.price = int(input("받을 돈을 입력하세요 : "))
        self.total = int(input("실제 받은 돈을 입력하세요 : "))
        self.left = self.total-self.price
        if self.left < 0:
            print("받은 돈이 부족합니다. 거스름돈 계산 프로그램을 종료합니다.")
            sys.exit(1)

    def cal_left(self):
        locate=0
        while self.left>0 and locate<8:
            if self.left // self.money[locate] > 0:
                self.money_left[locate] = self.left // self.money[locate]
                self.left %= self.money[locate]
            locate+=1
    
    def status(self):
        name = ["오만원 지폐", "만원 지폐", "오천원 지폐", "천원 지폐", "오백원 동전", "백원 동전", "오십원 동전", "십원 동전"]
        print("현재 받을 돈 {}원, 실제로 받은 돈은 {}원 입니다.".format(self.price, self.total))
        print("{}원을 거슬러줘야 합니다.".format(self.total-self.price))
        for i in range(8):
            if self.money_left[i]>0:
                print("{} {}{}".format(name[i], self.money_left[i], ("장" if i<4 else "개")))

my_change = Change()
my_change.cal_left()
my_change.status()