#include <stdio.h>
int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int a = n;
    while (1){
        int b = n%a;
        if(b==0 && m%a==0) break;
        a--;
    }
    printf("%d", a);
}