#include <stdio.h>
// // 지역변수
// int a = 1;
// void PPP(){
//     printf("function %d\n", a);
// }
// void main(){
//     PPP();
// printf("main %d", a);
// }

// int result = 0;
// void Sum(int data1, int data2){
//     // int result;
//     result = data1 + data2;
// }   
// void main(){
    
//     Sum(5,3);
//     printf("5+3 = %d\n", result);
// }

// void Test(){
//     static int data = 0;
//     printf("%d, ", data++);
// }
// void main(){
//     int i ;
//     for (i=0; i<5; i++){
//         Test();
//     }
// }
void main(){
    unsigned int a = 0x12345678, b = 0x12345678;
    unsigned char c = 0x48, d = 0x00;
    a = c;
    d = (unsigned char) b;
    printf("%d %d %d %d", a,b,c,d);
}