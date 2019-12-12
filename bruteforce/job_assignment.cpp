#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int cnt, ans;
vector<int> assign_cnt, assign;
vector<vector<int>> cost;

void get_min(int locate, int nowcost){
    if(nowcost>ans) return;
    if(locate==cnt){
        if(nowcost<ans){
            ans = nowcost;
            assign=assign_cnt;
        }
        return;
    }
    for(int i=0;i<cnt;i++){
        bool is_already_assign = false;
        for(int already : assign_cnt){
            if(already==i) is_already_assign = true;
        }
        if(!is_already_assign){
            assign_cnt.push_back(i);
            get_min(locate+1, nowcost+cost[locate][i]);
            assign_cnt.pop_back();
        }
    }
}

int main(){
    cout << "인원수(작업수)를 입력하세요 : ";
    cin >> cnt;

    for(int i=0; i<cnt; i++){
        vector<int>element(cnt);
        cost.push_back(element);
    }

    cout << "각 인원의 소요 비용을 입력해주세요." << endl;
    cout << "입력 형식은 다음과 같습니다." << endl;
    cout << "9 2 7 8" << endl;
    cout << "=> 한 인원의 각 작업 비용이 9, 2, 7, 8입니다."<< endl;
    int localmax=0;
    for(int i=0;i<cnt;i++){
        cout << "=> ";
        for(int j=0;j<cnt;j++){
            cin >> cost[i][j];
            localmax=max(localmax, cost[i][j]);
        }
    }
    ans = localmax*cnt;

    get_min(0, 0);
    for(int i=0;i<cnt;i++){
        cout << i+1 << "번 사람은 " << assign[i]+1 << "번 작업을 해야합니다." << endl;
    }
    cout << "총 비용은 " << ans << " 입니다.";
}