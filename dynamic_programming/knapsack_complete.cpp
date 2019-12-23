#include <iostream>
#include <vector>

using namespace std;
class Knapsack{
private:
    vector<pair<int, int>> probs; // 무게, 가치
    vector<int> frac, rank, check;
    int bag;

    void get_vpw(){
        frac.clear();
        rank.clear();
        check.clear();
        for(auto p : probs){
            frac.push_back(p.second/(double)p.first);
            check.push_back(0);
        }
        for(int i=0;i<frac.size();i++){
            int now = 0, locate;
            for(int j=0;j<frac.size();j++){
                if(!check[j] && now<=frac[j]){
                    locate=j;
                    now = frac[j];
                }
            }
            check[locate]=1;
            rank.push_back(locate);
        }
    }
    void get_vrank(){
        rank.clear();
        check.clear();
        for(auto p : probs){
            check.push_back(0);
        }
        for(int i=0;i<probs.size();i++){
            int now = 0, locate, w = 0;
            for(int j=0;j<probs.size();j++){
                if(!check[j] && now<=probs[j].second){
                    if(now==probs[j].second && w<probs[j].first) continue;
                    locate=j;
                    now = probs[j].second;
                    w = probs[j].first;
                }
            }
            check[locate]=1;
            rank.push_back(locate);
        }
    }

public:
    Knapsack(){
        cout << "가방의 가용 가능 무게를 입력하세요 : ";
        cin >> bag;

        cout << "무게와 가치를 입력해주세요." << endl;
        cout << "예) 10 30 (무게 10, 가치 30)" << endl;
        cout << "입력을 종료할려면 0 0을 입력해주세요." << endl;
        while (true){
            int w, v;
            cout << " => ";
            cin >> w >> v;
            if(w==v && v==0) break;
            probs.emplace_back(w, v);
        }
    }

    int bruteforce(int locate, int n, int w, int vsum, int wsum){
        if(locate==n){
            return vsum;
        }
        int ans = -1;
        if(wsum+probs[locate].first<=w){
            int tmp = bruteforce(locate+1, n, w, vsum+probs[locate].second, wsum+probs[locate].first);
            ans = (ans>tmp)?ans:tmp;
        }
        int tmp = bruteforce(locate+1, n, w, vsum, wsum);
        ans = (ans>tmp)?ans:tmp;
        return ans;
    }

    int greedy(bool isvpw){
        if(isvpw) get_vpw();
        else get_vrank();
        int nowbag = 0, value=0;
        for (auto r : rank){
            if(probs[r].first<=bag-nowbag){
                value += probs[r].second;
                nowbag += probs[r].first;
            }
        }

        return value;
    }

    int fractional(){
        get_vpw();
        int nowbag = 0, l=0, value = 0;
        while (l<probs.size() && nowbag<bag){
            if(probs[rank[l]].first<=bag-nowbag){
                value += probs[rank[l]].second;
                nowbag += probs[rank[l]].first;
            } else{
                value += frac[rank[l]] * (bag-nowbag);
                nowbag = bag;
            }
            l++;
        }
        return value;
    }

    int dynamic_programming(){
        vector<vector<int>> dp;
        for(int i=0;i<probs.size();i++){
            vector<int> tmp;
            for(int j=0;j<=bag;j++){
                tmp.push_back(0);
            }
            dp.push_back(tmp);
        }

        for(int i=0;i<probs.size();i++){
            for(int j=1;j<=bag;j++){
                if(i){
                    dp[i][j] = (probs[i].first<=j)?max(dp[i-1][j], dp[i-1][j-probs[i].first]+probs[i].second):dp[i-1][j];
                } else {
                    dp[i][j] = (probs[i].first<=j)?probs[i].second:0;
                }
            }
        }
        return dp[probs.size()-1][bag];

    }

    void menu(){
        while (true){
            int choice;
            cout << "원하시는 문제 풀이 방식을 입력해주세요." << endl;
            cout << "1) Brute Force (with Backtraking)" << endl;
            cout << "2) Greedy - 0/1" << endl;
            cout << "3) Greedy - 0/1 무게당 가치" << endl;
            cout << "4) Greedy - 0/1 무게당 가치 for fractional value" << endl;
            cout << "5) Dynamic Programming" << endl;
            cout << "9) 종료 " << endl;
            cout << " =>";
            cin >> choice;
            int value;
            switch (choice){
                case 1:
                    value = bruteforce(0, probs.size(), bag, 0, 0);
                    break;
                case 2:
                    value = greedy(false);
                    break;
                case 3:
                    value = greedy(true);
                    break;
                case 4:
                    value = fractional();
                    break;
                case 5:
                    value = dynamic_programming();
                    break;
                case 9:
                    exit(0);
                default:
                    cout << "입력을 잘못하셨습니다. 다시 입력해주세요.\n\n";
                    continue;
            }
            cout << "결과는 " << value << " 입니다.\n\n";
        }
    }
};

int main(){
    Knapsack my_knapsack;
    my_knapsack.menu();
}