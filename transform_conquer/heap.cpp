#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Heap{
private:
    vector<int> array;
    bool isMax;

public:
    Heap(bool imax){
        isMax = imax;
    }
    int size() {
        return array.size();
    }
    void insert(int data){
        array.push_back(data);
        int locate = size()-1;
        while(locate>0) {
            int parent = (locate - 1) / 2;
            if (array[parent] > array[locate] == isMax) break;
            swap(array[parent], array[locate]);
            locate = parent;
        }
    }
    int pop(){
        if(array.empty()) return -1;
        int locate = 0;
        int out = array[locate];
        array[locate] = array[size()-1];
        array.pop_back();
        while (locate < size()){
            int left = locate*2+1;
            int right = left+1;
            if(left>=size()) break;
            if(right==size()){
                if((array[left]>array[locate])==isMax) swap(array[left], array[locate]);
                break;
            }
            if(isMax){
                if(array[locate]>=array[left] && array[locate]>=array[right]) break;
                if(array[right]<array[left]){
                    swap(array[locate], array[left]);
                    locate=left;
                } else{
                    swap(array[locate], array[right]);
                    locate=right;
                }
            } else{
                if(array[locate]<=array[left] && array[locate]<=array[right]) break;
                if(array[right]>array[left]){
                    swap(array[locate], array[left]);
                    locate=left;
                } else{
                    swap(array[locate], array[right]);
                    locate=right;
                }
            }
        }
        return out;
    }
    void asort(){
        if(array.empty()){
            cout << "빈 배열입니다." << endl;
            return;
        }
        while (size()>0){
            cout << pop() << ' ';
        }
        cout << endl;
    }
    void status(){
        cout << "현재 힙 상황" << endl;
        cout << "현재 힙은 " << (isMax?"최대":"최소") << " 힙 입니다." << endl;
        int slash = 1;
        for(int i=0;i<size();i++){
            cout << array[i] << ' ';
            if(i!=size()-1){
                if(i==pow(2, slash)-2){
                    cout << "/ ";
                    slash++;
                } else cout << ", ";
            }
        }
        cout << endl << "총 노드 개수 : " << size() << "개" << endl;
    }
};

int main(){
    int isMax;
    bool is_continue=true;

    cout << "어떤 힙을 실행해보겠습니까?" << endl;
    cout << "1은 최대힙, 2는 최소힙입니다 : ";
    cin >> isMax;
    Heap my_heap(isMax==1);
    while (is_continue){
        int choice, data;

        cout << endl << "====MENU====" << endl;
        cout << "1. 데이터 추가" << endl;
        cout << "2. 데이터 삭제 (최상 노드만 가능)" << endl;
        cout << "3. 현제 힙 상태 보기" << endl;
        cout << "4. 데이터 모두 삭제 - 정렬 결과 확인 후 프로그램 종료" << endl;
        cout << " => ";
        cin >> choice;
        cout << "============" << endl << endl;

        switch(choice){
            case 1:
                cout << "추가될 데이터를 입력하세요 (자연수) : ";
                cin >> data;
                my_heap.insert(data);
                cout << "추가되었습니다!" << endl << endl;
                break;
            case 2:
                data = my_heap.pop();
                if(data==-1) cout << "빈 힙이기 때문에 데이터를 꺼낼 수 없습니다.";
                else cout << "삭제된 데이터는 " << data << "입니다.";
                cout << endl << endl;
                break;
            case 3:
                my_heap.status();
                break;
            case 4:
                cout << "최종 힙 정렬은" << endl;
                my_heap.asort();
                cout << "입니다.";
                is_continue = false;
        }
    }
}