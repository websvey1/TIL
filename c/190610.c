#include <stdio.h>
#include <string.h>
// // 단어 happy를 배열로 표시
// void main(){
//     char data[6] = { 'h','a','p','p','y'};
//     char data_2[6] = "happy";
//     printf("%d", sizeof(data));
//     printf("%c", data_2[1]);
// }
// // str 길이 구하는 함수 작성 및 사용
// int Getstr(char data[ ]){
//     int count = 0;
//     while (data[count]) count++;
//     return count;
//     }

// void main(){
//     int data_length;
//     char data[10] = {'h','a','p','p','y',0,};
//     char result[16];
//     data_length = Getstr(data);
//     strcpy(result, data);
//     strcat(result, "add");
//     printf("data length = %d\n", data_length);
//     printf("strlen = %d\n", strlen(data));
//     printf("%s + \"def\" = %s\n", data, result);
// }
// hello배열을 이용해 hello world 만들어보기
// int main(){
//     char data[10] = "hello";
//     char result[20];
//     strcpy(result, data);
//     strcat(result, " world");
//     printf("%s + \"world\" = %s", data,result);
// }

// 2차원배열
// int main(){
//     char data[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
//     printf("%d", data[2][2]);
// }

// // 1차원 배열과 2차원 배열의 차이 ( 3행 4열로 가정)
// void main(){
//     char data[12] = {0,0,2,0,1,1,0,0,2,1,0,2};
//     int i,x,y;
//     for (i=0; i<12; i++){
//         x = i%4+1; // 1 2 3 4  1 2 3 4 순환   열
//         y = i/4+1; // 1 1 1 1  2 2 2 2  3 3 3 3 행
//         printf("%drow %dcol ", y,x);
//         if (data[i]==1) printf("black\n");
//         else if (data[i]==2) printf("white\n");
//         else printf("no \n");
//     }
// }
// void main(){
//     char data[3][4] = {{0,0,2,0},{1,1,0,0},{2,1,0,2}};
//     int x,y;
//     for (x=0; x<3; x++){
//         for (y=0; y<4; y++){
//             printf("%drow %dcol ", x+1,y+1);
//             if (data[x][y]==1) printf("black\n");
//             else if (data[x][y]==2) printf("white\n");
//             else printf("no \n");
//         }        
//     }
// }
// int main(){
//     char data[9] = {4,6,9,8,7,2,5,1,3};
//     char i, hap, lll, mmaaxx;
//     hap = 0;
//     lll = strlen(data)-1;
//     // for (i=0; i<lll;i++){
//     //     if (i%2) continue;
//     //     else hap +=data[i];
//     // }
//     mmaaxx = data[0];
//     for (i=1; i<lll; i++){
//         if (data[i] > mmaaxx) mmaaxx = data[i];
//         // printf("%d", mmaaxx);
//     }
//     printf("%d", mmaaxx);
// }

// // 3 x 4 배열이 data[3][4]가 맞는지 테스트 = > data[3][4]는 4X5이다 !
// int main(){
//     char data[3][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0}};
//     char i,j;
//     for (i=0; i<=3; i++){
//         for (j=0; j<=4; j++){
//             printf("%d %d  = %d\n", i,j,data[i][j]);
//         }
//     }
// }

//  정렬하기
int main(){
    int data[7] = {6,3,9,7,2,4,1};
    char i, j, tmp;
    for (i=0; i<7; i++){
        for (j=i+1; j<7; j++){
            if (data[i] > data[j]){
                tmp = data[i];
                data[i] = data[j];
                data[j] = tmp;
            }
        }
    }
    for (i=0; i<7; i++){
        printf("%d " , data[i]);
    }
}

