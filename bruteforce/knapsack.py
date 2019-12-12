# Knapsack Problem in Python
# 입, 출력 형식은 위 C 코드에서 정의한 형식과 동일합니다.

weight=[]
value=[]

def go(locate, n, w, vsum, wsum):
    global weight, value

    if locate==n:
        return vsum
    ans = -1

    if wsum+weight[locate]<=w:
        tmp = go(locate+1, n, w, vsum+value[locate], wsum+weight[locate])
        ans = max(ans, tmp)

    tmp = go(locate+1, n, w, vsum, wsum)
    ans = max(ans, tmp)

    return ans

# Main Part
n, w = map(int, input('').split())

for i in range(n):
    tmpw, tmpv = map(int, input('').split())
    weight.append(tmpw)
    value.append(tmpv)

print(go(0, n, w, 0, 0))