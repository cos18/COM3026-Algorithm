# Python
import random
import time

player = 0

def check_jjak(n):
    return (1 if (n%10%3==0 and n%10!=0) else 0) + (check_jjak(n//10) if n>=10 else 0)

def print_player(times):
    global player

    now_player = (times-1)%player + 1
    print("Player {} : ".format(now_player), end='')
    check = check_jjak(times)
    if check:
        print("짝"*check)
    else:
        print(i)

    if now_player == player:
        print("")

startTime = time.time()

# Main Part
print(">>> 3-6-9 게에임! <<<\n")
player = int(input("Player 수를 입력하세요 : "))
endnum = int(input("끝나는 수를 입력하세요 : "))

print("\n>>>시작<<<")

for i in range(1, endnum+1):
    print_player(i)

print(">>>종료<<<\n")

endTime = time.time() - startTime
print('Time : ', endTime)