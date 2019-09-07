#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int number[500];

void merge(int start, int mid, int end){
    int* sort_array = (int*)malloc(sizeof(int)*(end-start+1));
    int locate = 0, start_location = start, end_location = mid+1;
    while(start_location<=mid && end_location<=end){
        if(number[start_location]>number[end_location]){
            sort_array[locate++] = number[start_location];
            start_location++;
        } else {
            sort_array[locate++] = number[end_location];
            end_location++;
        }
    }
    while(start_location<=mid){
        sort_array[locate++] = number[start_location++];
    }
    while(end_location<=end){
        sort_array[locate++] = number[end_location++];
    }
    for(int i=start;i<=end;i++){
        number[i] = sort_array[i-start];
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
    int size=0;
    for(int i=0;i<500;i++){
        number[i] = rand()%1000000+1;
        printf("%3d번째 숫자 : %6d\n", i+1, number[i]);
    }
    sort(0, 499);
    printf("5번쨰 큰 수는... %d!\n", number[4]);

    clock_t end = clock();
    printf("\nTime : %lf\n", (double)(end - start)/CLOCKS_PER_SEC);
}