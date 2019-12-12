import copy

cnt = 0
ans = 0
assign_cnt=[]
assign=[]
cost=[]

def get_min(locate, nowcost):
    global cnt, ans, assign, assign_cnt, cost
    if nowcost>ans:
        return
    if locate==cnt:
        if nowcost<ans:
            ans = nowcost
            assign=copy.deepcopy(assign_cnt)
        return

    for i in range(cnt):
        if not i in assign_cnt:
            assign_cnt.append(i)
            get_min(locate+1, nowcost+cost[locate][i])
            assign_cnt.pop()
        
# Main Part
cnt = int(input("인원수(작업수)를 입력하세요 : "))

print("각 인원의 소요 비용을 입력해주세요.")
print("입력 형식은 다음과 같습니다.")
print("9 2 7 8")
print("=> 한 인원의 각 작업 비용이 9, 2, 7, 8입니다.")
localmax=0

for i in range(cnt):
    cost.append(list(map(int, input('=> ').split())))
    for j in cost[len(cost)-1]:
        localmax = max(localmax, j)

ans = localmax*cnt

get_min(0, 0)
for i in range(cnt):
    print(i+1, "번 사람은", assign[i]+1, "번 작업을 해야합니다.")

print("총 비용은" ,ans, "입니다.")
