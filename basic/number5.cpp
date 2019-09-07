/*
 * 190905 과제
 * 코딩1 : 넘버 5
 * Input : N/A
 * Processing
 * 1,000,000 보다 작은 수 500개를 랜덤하게 생성
 * 생성된 수 가운데 5번째로 큰 수 찾기
 * Output : 넘버 5 출력
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int top5[6]={1000001, 1000001, 1000001, 1000001, 1000001, 1000001};

void merge(int start, int mid, int end){
    int* sort_array = (int*)malloc(sizeof(int)*(end-start+1));
    int locate = 0, start_location = start, end_location = mid+1;
    while(start_location<=mid && end_location<=end){
        if(top5[start_location]>top5[end_location]){
            sort_array[locate++] = top5[start_location];
            start_location++;
        } else {
            sort_array[locate++] = top5[end_location];
            end_location++;
        }
    }
    while(start_location<=mid){
        sort_array[locate++] = top5[start_location++];
    }
    while(end_location<=end){
        sort_array[locate++] = top5[end_location++];
    }
    for(int i=start;i<=end;i++){
        top5[i] = sort_array[i-start];
    }
    free(sort_array);
}

void sort(int start, int end){
    int mid;
    if(start < end) {
        mid = (start + end)/2;
        sort(start, mid);
        sort(mid+1, end);
        merge(start, mid, end);
    }
}

int main(){
    clock_t start = clock();
    srand((unsigned int)time(NULL));
    int number[500], size=0;
    for(int i=0;i<500;i++){
        number[i] = rand()%1000000+1;
        printf("%3d번째 숫자 : %6d\n", i+1, number[i]);
    }
    for(int i=0;i<500;i++){
        top5[size++] = number[i];
        sort(0, size-1);
        if(size>5) size = 5;
    }
    printf("5번쨰 큰 수는... %d!\n", top5[4]);

    clock_t end = clock();
    printf("\nTime : %lf\n", (double)(end - start)/CLOCKS_PER_SEC);
}