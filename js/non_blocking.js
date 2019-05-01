
// // 1 //
// const nothing = () => {}
// console.log('start sleeping')
// setTimeout(nothing, 3000) // 멈추지 않음. callback stack에 들어가 3초를 실행하고 있기때문에
//                           // 사용자 입장에선 바로 실행되는것처럼 보임
//                           // 해당 함수 시작 이후 종료까지 기다리지 않고 바로 다음줄의 코드를 실행!
// console.log('end of program')

// // like python
// //2//
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)
// /*      
// 1은 nothin함수에 아무것도 없어서 3초가 지연되지 않지만
// 2는 logEnd함수에 end of program 메세지가 들어있어서 3초 후 출력된다.
// */
// // 3 //
// function first() {
//     console.log('first')
// }
// function second() {
//     console.log('second')
// }
// function third() {
//     console.log('third')
// }
// first()
// setTimeout(second, 1000) // 0으로 바꿔도, first -> third -> second 순서로 실행된다
//                          // callback함수
// third()
// /* 1. 호출한 것은 call stack에 쌓인다
//    2. setTimeout은 콜백함수여서 callback stack으로 간다.
//    3. 그렇지 않은 것을 다시 호출해서 쌓인다.
//    4. 이벤트 루프가 call stack이 empty할때까지 기다린다
//    5. call stack이 empty상태면 callback stack의 리턴값을 call stack에 넣는다.
//  */

 function func3() {
     console.log('func3')
 }
 function func2() {
    setTimeout(console.log, 1000, 'func2')
    func3()
}   

function func1() {
    console.log('func1')
    func2()
}
func1()