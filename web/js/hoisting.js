// let 블록스코프 예제

// {
//     let x = 'HO'
//     console.log(x) //  HO
//     {
//         let x = 1
//         console.log(x) // 1
//     }
//     console.log(x) // HO
// }
// console.log(typeof x) //  에러
 

// // 같은 조건에서 let을 var로 바꾼다면 
// {
//     var x = 'HO'
//     console.log(x) //  HO
//     {
//         var x = 1
//         console.log(x) // 1
//     }
//     console.log(x) // HO                 // 이부분이 1로 바뀐다.
// }
// console.log(typeof x) //  에러            // 여기도 에러없이 타입이 number로 바뀐다.



/////////////////////////////////////////////////////////
// a 
// let a = 1
// a
// //출력하면 에러

// b
// var b = 1
// b
// //출력하면 에러가 나지 않고 1이 나옴

// //js가 이해한 코드
// var b      // hoisting , 변수를 할당하지 않고 일단 끌어올림(할당X, 선언만)
// b // undefined
// b = 1  // 1
// b    // 1


// if (x !== 1) {
//     console.log(y)   // undefined
//     var y=3
//     if (y===3) {
//         var x = 1
//     }
//     console.log(y)    // 3
// }
// if (x===1){
//     console.log(y)  // 3
// }
// // var로 변수를 선언하면 자바스크립트는 변수를 여러번 정의하더라도
// // 무시한다
// var x = 1
// if (x===1){
//     var x = 2
//     console.log(x)  // 2
// }
// console.log(x)  // 2
// //////////////////////////////////////////////////////////////////

// function hoisting
ssafy()
function ssafy() {
    console.log('hoisting!!!')
}
