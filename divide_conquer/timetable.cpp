#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

void check(int start, int end, int *checktime){
    if(start==end){
        checktime[start]++;
        return;
    }
    int mid = (start+end)/2;
    check(start, mid, checktime);
    check(mid+1, end, checktime);
}

int main() {
    cout << "몇 명인가요? ";
    int person;
    cin >> person;
    vector<pair<int, int>> timetable[10][5];
    for (int i = 0; i < person; i++) {
        while (true) {
            string line;
            cin.clear();
            getline(cin, line);
            if (line==".") break;

            istringstream buf(line);
            istream_iterator<string> beg(buf), fin;
            vector<string> tokens(beg, fin);

            int day = 0;
            for(auto& s: tokens){
                if(s[0]>='0' && s[0]<='9'){
                    int start = stoi(s.substr(0, 4)), end = stoi(s.substr(5));
                    start = (start/100-9)*12+start%100/5;
                    end = (end/100-9)*12+end%100/5;
                    timetable[i][day].emplace_back(start, end);
                } else{
                    if(s=="MON"){
                        day = 0;
                    } else if (s=="TUE"){
                        day = 1;
                    } else if (s=="WED"){
                        day = 2;
                    } else if (s=="THU"){
                        day = 3;
                    } else{
                        day = 4;
                    }
                }
            }
        }
    }

    for(int day=0;day<5;day++){
        vector<pair<int, int>> gonggang;
        int checktime[145]={};
        for(int p=0;p<person;p++){
            for(auto& s: timetable[p][day]){
                check(s.first, s.second, checktime);
            }
        }
        int start=-1;
        for(int i=0;i<145;i++){
            if(start==-1 && checktime[i]==0) start=((i==0)?0:i-1);
            if(start!=-1 && checktime[i]>0){
                if(i-start>=6){
                    gonggang.emplace_back(start, i);
                }
                start = -1;
            }
        }
        if(start!=-1 && 144-start>=6){
            gonggang.emplace_back(start, 144);
        }
        if(!gonggang.empty()){
            switch(day){
                case 0:
                    cout << "MON ";
                    break;
                case 1:
                    cout << "TUE ";
                    break;
                case 2:
                    cout << "WED ";
                    break;
                case 3:
                    cout << "THU ";
                    break;
                case 4:
                    cout << "FRI ";
                    break;
            }
            for(auto& t: gonggang){
                cout << setw(2) << setfill('0') << t.first/12+9 << setw(2) << setfill('0') << t.first%12*5
                    << "-" << setw(2) << setfill('0') << t.second/12+9 << setw(2) << setfill('0') << t.second%12*5 << ' ';
            }
            cout << endl;
        }
    }
}