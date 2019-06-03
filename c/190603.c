#include <stdio.h>

// for기본
// void main(){
//     int sum=0, num;
//     for (num = 1; num<=5; num++){
//         printf("num(%d) + sum(%d) = ", num,sum);
//         sum +=num;
//         printf("%d\n", sum);
//     }
// }

// // while
// void main(){
//     int sum=0, num=1;
//     while (num<=5){
//         printf("num(%d) + sum(%d) = ", num,sum);
//         sum +=num;
//         printf("%d\n", sum);
//         num++;
//     }
// }

// //while로 안녕하세요 10번 출력
// void main(){
//     int cnt = 0;
//     while (cnt <= 10){
//         printf("hi \n");
//         cnt++;
//     }
// }

// 구구단 만들기
// void Gop(int n){
//     int start = n, gop = 1, result = 1;
//     while (gop <10){
//         printf("%d * %d = ", start, gop);
//         result = start * gop;
//         printf("%d\n", result);
//         gop ++;
//     }
// }
// void main(){
//     int s;
//     for (s = 2; s<=9; s++){
//         Gop(s);
//     }    
// }
/* 파이썬코드
for i in range(1,10):
	r = a*i
	print("%d * %d = %d" %(a,i,r))
*/

// // 반복문 빠져나오기 break 이중
// void main(){
//     int m,n;
//     for(m=5; m<7; m++){
//         for (n=0; n<3; n++){
//             if (m==5 && n==1) break;
//             printf("m(%d) - n(%d)\n", m,n);
//         }
//         if (m==5 && n==1) break;
//     }
// }

// // continue
// void main(){
//     int a ;
//     for (a = 1; a<10 ; a++){
//         if (a == 3 || a == 5) continue;
//             printf("%d\n", a);
        
//     }
// }

