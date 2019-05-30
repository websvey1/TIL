
#include <stdio.h>
// // ++i와 i++
// int main(){
//     int i = 1;
//     printf("%d", i++);
// }
// // 관계연산자 boolean
// void main(){
//     int d1 = 5, d2 = 3;
//     int r1 = d1 > 7;
//     int r2 = d2 <= d1;
//     int r3 = d2 == 7;
//     int r4 = d2 != d1;
//     printf("result : %d, %d, %d, %d\n", r1, r2, r3, r4);
// }

// // 논리연산자
// int main(){
//     int d1=5, d2=3;
//     int r1 = 0 ||1;
//     int r2 = 3 && -1;
//     int r3 = d1==3 || d2==3;
//     int r4 = d1 == 3 && d2==3;
//     printf("%d %d %d %d", r1,r2,r3,r4);
// }
// // 연산자 우선순위
// int main(){
//     int d = 5, r = 0;
//     r = r-- || (d=1);
//     printf("%d %d", d,r);

// }
// 복합 조건문
// void main(){
//     int score = 82;
//     char grade;
//     if (score >=90) {
//         grade = 'A';
//         printf("score is %d, grade is %c \n", score, grade);
//     }
//     printf("END\n");

// }
// // 줄이기
// void main(){
//     int s = 86;
//     char g;
//     if (s >=90) g = 'A';
//     else {
//         if (s >=80) g='B';
//         else {
//             if (s >=70) g = 'C';
//             else g = 'D';
//         }
//     }
// }
// void main(){
//     int s = 86;
//     char g;
//     if (s >=90) g = 'A';
//     else if (s >=80) g='B';
//     else if (s >=70) g = 'C'; // 파이썬의 elif
//     else g = 'D';
// }
// // switch문
// void main() {
//     int score = 86;
//     char grade;
//     switch(score/10){
//         case 10:
//         case 9:
//             grade = 'A';
//             break;
//         case 8:
//             grade = 'B';
//             break;
//         case 7:
//             grade = 'C';
//             break;
//         case 6:
//             grade = 'D';
//             break;
//         default:
//             grade = 'F';
//             break;
//     }
//     printf("%d %c \n", score, grade);
// }
void main(){
    int result = -4;
    // if (result<0){
    //     result *= -1;
    //     printf("%d", result);
    result = (result<0) ? result *-1 : result*1;
        printf("%d", result);
    }
