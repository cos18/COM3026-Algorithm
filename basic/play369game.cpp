/*
 * 코딩2 : 3-6-9 게임
 * - Input
 *   Player 수
 *   끝나는 수
 * - Processing
 *   반복문
 *   조건문
 * - Output
 *   Player와 외치는 값
 *   박수 표현
 */
#include <stdio.h>
#include <time.h>

int check_jjak(int n){
    return ((!(n%10%3) && (n%10))?1:0) + ((n>=10)?check_jjak(n/10):0);
}

int main(){
    int player=3, endnum=35;
    printf(">>> 3-6-9 게에임! <<<\n");

    // 입력 부분을 주석해제하여 직접 숫자를 입력할 수 있음.
    /*
    printf("Player 수를 입력하세요 : ");
    scanf("%d", &player);
    printf("끝나는 수를 입력하세요 : ");
    scanf("%d", &endnum);
     */

    clock_t start = clock();

    printf("\n\n>>>시작<<<\n");
    for(int i=1;i<=endnum;i++){
        printf("Player %d : ", (i-1)%player+1);
        int check = check_jjak(i);
        if(check){
            for(int i=0;i<check;i++) printf("짝");
        } else printf("%d", i);
        printf("\n");
        if((i-1)%player+1 == player) printf("\n");
    }
    printf(">>>종료<<<\n");

    clock_t end = clock();
    printf("\nTime : %lf\n", (double)(end - start)/CLOCKS_PER_SEC);
}