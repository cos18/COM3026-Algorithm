#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Change{
private:
    int money[8] = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
    int money_left[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int price, total, left;

    void cal_left(){
        for(int locate=0;locate<8;locate++){
            if(left/money[locate]>0){
                money_left[locate] = left/money[locate];
                left %= money[locate];
            }
            if(left==0) break;
        }
    }

public:
    Change(int p, int t){
        price = p;
        total = t;
        left = total-price;
        cal_left();
    }

    void status(){
        vector<string> name = {"오만원 지폐", "만원 지폐", "오천원 지폐", "천원 지폐", "오백원 동전", "백원 동전", "오십원 동전", "십원 동전"};
        cout << endl << "현재 받을 돈 " << price << "원, 실제로 받은 돈은 " << total << "원 입니다." << endl;
        cout << total-price << "원을 거슬러줘야 합니다." << endl << endl;
        for(int i=0;i<8;i++){
            if(money_left[i]>0){
                cout << name[i] << " " << money_left[i] << (i<4?"장":"개") << endl;
            }
        }
    }
};

int main(){
    int p, t;
    cout << "받을 돈을 입력하세요 : ";
    cin >> p;
    cout << "실제 받은 돈을 입력하세요 : ";
    cin >> t;
    if(t-p<0){
        cout << "받은 돈이 부족합니다. 거스름돈 계산 프로그램을 종료합니다.";
        return 0;
    }
    Change my_change = Change(p, t);
    my_change.status();
}