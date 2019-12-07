#include <iostream>

using namespace std;

int map[10002];
int dp[10001][7][7]={};
int panmove[7][7]={
        {},
        {0, 0, 1, 2, 1, 2, 3},
        {0, 1, 0, 1, 2, 1, 2},
        {0, 2, 1, 0, 3, 2, 1},
        {0, 1, 2, 3, 0, 1, 2},
        {0, 2, 1, 2, 1, 0, 1},
        {0, 3, 2, 1, 2, 1, 0}
};
int ans = 30001;

void findpath(int x, int y, int locate, int moving);
int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int locate;
    cin >> locate;
    for(int i=1;i<=locate;i++){
        cin >> map[i];
    }
    for(int k=0;k<=locate;k++) {
        for (int i = 1; i < 7; i++) {
            for (int j = 1; j < 7; j++) {
                dp[k][i][j]=-1;
            }
        }
    }
    dp[0][1][3] = 0;
    for(int now=1;now<=locate;now++){
        for(int i=1;i<7;i++){
            for(int j=1;j<7;j++){
                if(dp[now-1][i][j]!=-1){
                    if(map[now]!=j){
                        int i_dp = dp[now-1][i][j] + panmove[i][map[now]];
                        if(dp[now][map[now]][j]!=-1){
                            dp[now][map[now]][j] = (dp[now][map[now]][j]>i_dp)?i_dp:dp[now][map[now]][j];
                        } else dp[now][map[now]][j] = i_dp;
                    }

                    if(map[now]!=i){
                        int j_dp = dp[now-1][i][j] + panmove[j][map[now]];
                        if(dp[now][i][map[now]]!=-1){
                            dp[now][i][map[now]] = (dp[now][i][map[now]]>j_dp)?j_dp:dp[now][i][map[now]];
                        } else dp[now][i][map[now]] = j_dp;
                    }

                }
            }
        }
    }
    int finali=0, finalj=0;
    for(int i=1;i<7;i++){
        for(int j=1;j<7;j++){
            if(dp[locate][i][j]!=-1){
                if(ans>dp[locate][i][j]){
                    ans = dp[locate][i][j];
                    finali=i;
                    finalj=j;
                }
            }
        }
    }
    findpath(finali, finalj, locate, ans);
    cout << "<" << finali << ", " << finalj << ">" << endl;
    return 0;
}

void findpath(int x, int y, int locate, int moving){
    if(x==y && y==0){
        cout << "ERROR";
        return;
    }
    if(locate==1){
        cout << "<" << x << ", " << y << "> -> ";
        return;
    }
    for(int i=1;i<7;i++){
        for(int j=1;j<7;j++){
            if(dp[locate-1][i][j]==-1) continue;
            int dmove = moving-dp[locate-1][i][j];
            if(dmove==panmove[i][map[locate]] || dmove==panmove[j][map[locate]]){
                findpath(i, j, locate-1, moving-dmove);
                if(moving!=ans) cout << "<" << x << ", " << y << "> -> ";
                return;
            }
        }
    }
}
