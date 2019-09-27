'''
Traveling Salesman Problem in Python
입,출력 예시는 백준 알고리즘 사이트의 '외판원순회2' 문제를 참고했습니다.
(링크 : https://boj.kr/tsp2)
'''

go = list()
check = list()
W = list()

N=0

# 갈 순서를 정해, 다 정하면 걸리는 비용의 최소값을 반환해준다.
def howtogo(turn):
    ans = 1000000*10+1; # 순회 가능한 최대값
    if turn==N:
        # 순서를 모두 정한 경우, 비용 계산
        if W[go[N-1]][go[0]]:
            ans = 0
            for i in range(N-1):
                ans += W[go[i]][go[i+1]]
            ans += W[go[N-1]][go[0]];
    else:
        for i in range(N):
            if check[i]: # 이 미 방문한 도시는 방문 필요 X
                continue 
            if turn and (not W[go[turn - 1]][i]): # 그 도시로 가는 길이 없으면 방문이 되지 않음
                continue 
            check[i] = 1
            go.append(i)
            tmp = howtogo(turn + 1)
            ans = tmp if (ans > tmp) else ans # 최소값이 맞는지 계산후 변수에 넣
            check[i] = 0
            go.pop()
    return ans

N = int(input())
for i in range(N):
    check.append(0)
    W.append(list(map(int, input().split())))
print(howtogo(0))