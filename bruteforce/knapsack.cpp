/*
 * Knapsack Problem in C
 *
 * - Input 형식
 * 첫줄에는 물건의 갯수와 제한 가방 무게를 입력합니다.
 * 이후 물건의 갯수 줄수만큼 그 물건의 무게와 가치를 입력합니다.
 *
 * - Output 형식
 * 최대 가치를 출력합니다.
 *
 * - Input 예시
 * 4 10
 * 7 42
 * 3 12
 * 4 40
 * 5 25
 *
 * - Output 예시
 * 65
 */
#include <iostream>

using namespace std;

int weight[20], value[20];
int go(int locate, int n, int w, int vsum, int wsum){
    if(locate==n){
        return vsum;
    }
    int ans = -1;
    if(wsum+weight[locate]<=w){
        int tmp = go(locate+1, n, w, vsum+value[locate], wsum+weight[locate]);
        ans = (ans>tmp)?ans:tmp;
    }
    int tmp = go(locate+1, n, w, vsum, wsum);
    ans = (ans>tmp)?ans:tmp;
    return ans;
}

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, w;
    cin >> n >> w;
    for(int i=0;i<n;i++){
        cin >> weight[i] >> value[i];
    }
    cout << go(0, n, w, 0, 0);
}