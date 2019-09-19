while True:
    k = input("x, y, z의 중복 여부를 입력해주세요. (yes/no) : ")
    if k=="yes" or k=="no":
        k = 1 if k=="yes" else 2
        break
    print("잘못 입력하셨습니다. 다시 입력하세요.")
cnt = 0
for x in range(1, 100-k):
    for y in range(1, 100-x):
        z=100-x-y
        if((k==2) and (x==y or y==z or z==x)):
            continue
        print("{} | {} | {}".format(x, y, z))
        cnt += 1

print("총 {}개".format(cnt))