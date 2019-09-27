/*
 * Traveling Salesman Problem in C
 * 입,출력 예시는 백준 알고리즘 사이트의 '외판원순회2' 문제를 참고했습니다.
 * (링크 : https://boj.kr/tsp2)
 */
#include <cstdio>
#include <vector>
using namespace std;

vector<int> go, check;
vector<vector<int>> W;

int N;

// 갈 순서를 정해, 다 정하면 걸리는 비용의 최소값을 반환해준다.
long long howtogo(int turn){
    int ans = 1000000*10+1; // 순회 가능한 최대값
    if(turn==N){
        // 순서를 모두 정한 경우, 비용 계산
        if(W[go[N-1]][go[0]]){
            ans = 0;
            for(int i=0;i<N-1;i++){
                ans += W[go[i]][go[i+1]];
            }
            ans += W[go[N-1]][go[0]];
        }
    } else {
        for (int i = 0; i < N; i++) {
            if (check[i]) continue; // 이미 방문한 도시는 방문 필요 X
            if (turn && !W[go[turn - 1]][i]) continue; // 그 도시로 가는 길이 없으면 방문이 되지 않음
            check[i] = 1;
            go.push_back(i);
            int tmp = howtogo(turn + 1);
            ans = (ans > tmp) ? tmp : ans; // 최소값이 맞는지 계산후 변수에 넣
            check[i] = 0;
            go.pop_back();
        }
    }
    return ans;
}

int main(){
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        vector<int> tmp;
        int numtmp;
        for(int j=0;j<N;j++){
            scanf("%d", &numtmp);
            tmp.push_back(numtmp);
        }
        W.push_back(tmp);
        check.push_back(0);
    }
    printf("%d\n", howtogo(0));
}