#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

ostream& operator<<(ostream& os, const vector<pair<int, int>>& vp)
{
    os << "[";
    for(int i=0;i<vp.size();i++){
        os << "[" << vp[i].first << ", " << vp[i].second << "]";
        if(i!=vp.size()-1) os << ", ";
    }
    os << "]";
    return os;
}

class Scheduler{
private:
    vector<pair<int, int>> tasks;
    vector<vector<pair<int, int>>> process;

public:
    Scheduler(){
        cout << "작업의 시작 시간과 끝 시간을 입력해주세요." << endl;
        cout << "예) 10 20" << endl;
        cout << "0 0을 입력하면 작업 입력이 종료됩니다." << endl;

        while (true){
            int s, e;
            cout << " => ";
            cin >> s >> e;
            if (s==e && e==0) break;
            if (s>=e){
                cout << "시작시간보다 끝나는 시간이 빠르거나 같을 수 없습니다." << endl;
                continue;
            }
            tasks.emplace_back(s, e);
        }
        sort(tasks.begin(), tasks.end());
    }
    void assign(){
        for(auto t : tasks){
            int locate = 0;
            while(locate<process.size()){
                if(process[locate].back().second <= t.first){
                    process[locate].push_back(t);
                    break;
                }
                locate++;
            }
            if(locate==process.size()){
                vector<pair<int, int>> newv;
                newv.push_back(t);
                process.push_back(newv);
            }
        }
    }
    void status(){
        for(int i=0;i<process.size();i++){
            cout << i+1 << "번 프로세서 : " << process[i] << endl;
        }
    }
};

int main(){
    Scheduler my_scheduler;
    my_scheduler.assign();
    my_scheduler.status();
}