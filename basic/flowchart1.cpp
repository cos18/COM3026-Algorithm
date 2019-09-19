#include <stdio.h>
int main(){
    int N;
    scanf("%d", &N);
    int M=1, F=1;
    while(1) {
        F = F * M;
        if (M == N) break;
        M++;
    }
    printf("%d", F);
}