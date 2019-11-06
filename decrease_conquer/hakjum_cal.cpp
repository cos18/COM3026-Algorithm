#include <iostream>
#include <locale>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// TODO : UTF-8 인코딩 형식의 txt파일을 읽어오고 쓰는 과정을 구현하지 못했습니다 ㅠㅠ...
// 이 코드에는 최대한 시도한 흔적을 남겨보았습니다.
// 파이썬 파일의 경우에는 파일 입출력이 구현되어있습니다.
// 이후 재재출 기회가 생긴다면 꼭 구현해보겠습니다!!

class Graduate{
private:
    vector<string> mlist;
    vector<string> glist {"../data/gyoil.txt", "../data/gyopil.txt"};
    vector<vector<string>> gyojic, major;
    int gyo_unit=22, gyo_nowunit, major_unit, major_nowunit, hakbun;
    void readFile(string file, vector<string> &at){
        wstring buff;
        wfstream fs(file);
        while ( getline(fs, buff) ) {
            string tmp;
            tmp.assign(buff.begin(), buff.end());
            if(tmp=="") break;
            at.push_back(tmp);
        }
        fs.close();
    }

public:
    Graduate(){
        for(string g : glist){
            vector<string> tmp;
            readFile(g, tmp);
            gyojic.push_back(tmp);
        }
        gyo_nowunit = ((int)gyojic[0].size()+(int)gyojic[1].size()-2)*2;

        while(true){
            cout << "단일/복수전공 여부를 입력해주세요" << endl << "1은 단일전공, 2는 복수전공입니다." << endl << ">> ";
            int select;
            cin >> select;
            if(select==1){
                major_unit = 66; break;
            } else if (select==2){
                major_unit = 50; break;
            } else{
                cout << "잘못 입력하셨습니다. 다시 입력해주세요." << endl;
            }
        }

        cout << "학번을 입력해주세요." << endl << "예를 들어, 18학번은 18을 입력해주세요." << endl << ">> ";
        cin >> hakbun;
        if(hakbun<17){
            mlist.push_back("../data/jeonil_old.txt");
            mlist.push_back("../data/jeonpil_old.txt");
        } else{
            mlist.push_back("../data/jeonil_new.txt");
            mlist.push_back("../data/jeonpil_new.txt");
        }

        for(auto m : mlist){
            vector<string> tmp;
            ifstream in(m);
            string s;
            while (in) {
                getline(in, s);
                tmp.push_back(s);
            }
            in.close();
            major.push_back(tmp);
        }
        major_nowunit = major_unit - (32-(int)mlist[0].size()-(int)mlist[1].size())*3+1;
        for(auto mp : major[1]){
            if(mp=="상업정보교과논리논술"){
                major_nowunit--;
                break;
            }
        }
    }

    void status(){
        cout << "===============\n남은 학점" << endl;
        cout << "   전공 " << major_nowunit << "/" << major_unit << endl;
        cout << "   교직 " << gyo_nowunit << "/" << gyo_unit << "\n\n";
        cout << "남은 전공필수 과목" << endl;
        for(auto m : major){
            for(auto lesson : m) cout << "   " << lesson << endl;
        }

        cout << "남은 교직필수 과목" << endl;
        for(auto lesson : gyojic[1]) cout << "   " << lesson << endl;
        cout << "===============" << endl;
    }

    bool listen_lesson(string lesson) {
        return false;
    }

    bool is_graduate(){
        return gyo_nowunit<=0 && major_nowunit<=0 && major[1].empty() && gyojic[1].empty();
    }
};

int main(){
    locale::global(locale("ko_KR.UTF-8")); // 맨 처음 한번 실행
    Graduate now;
    now.status();
    while (true){
        string cmd;
        cout << ">> ";
        cin.clear();
        getline(cin, cmd);
        if(cmd=="status" || now.listen_lesson(cmd)){
            now.status();
            if(now.is_graduate()){
                cout << "졸업!!!";
                return 0;
            }
        } else cout << "잘못 입력하셨습니다. 다시 입력해주세요." << endl << "입력 가능한 문자열은 문제 조건을 확인해주세요." << endl;
    }
}