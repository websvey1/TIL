//////////////////////////////////////////////////////////////   1       ////////////////////////////////////////////////////////
// // 배열로 이루어진 숫자들을 모두 더하는 함수
var numbers = [1,2,3,4,5,]

// const numbersAddEach = (numbers) => {
//     let sum = 0
//     for ( const number of numbers){
//         sum += number
//     }
//     return sum
// }
// numbersAddEach(numbers)
// console.log(numbersAddEach(numbers))


// // 배열로 이루어진 숫자들을 모두 빼는 함수
// const numbersSubEach = (numbers) => {
//     let sum = 0
//     for ( const number of numbers){
//         sum -= number
//     }
//     return sum
// }
// numbersSubEach(numbers)
// console.log(numbersSubEach(numbers))


// // 배열로 이루어진 숫자들을 모두 곱하는 함수
// const numbersMulEach = (numbers) => {
//     let sum = 1
//     for ( const number of numbers){
//         sum *= number
//     }
//     return sum
// }
// numbersMulEach(numbers)
// console.log(numbersMulEach(numbers))
//////////////////////////////////////////////////////////////   1       ////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////   222       ////////////////////////////////////////////////////////
// //숫자로 이루어진 배열의 요소들은 각각 [??]한다
const numbersEach = (numbers, callback) =>{
    let acc
    for (const number of numbers){
        acc= callback(number, acc) // 
    }
    return acc
}
// 더한다
const addEach = (number, acc=0) => {
    return acc + number
}
numbersEach(numbers, addEach)
console.log(numbersEach(numbers, addEach))

// //뺀다
// const subEach = (number, acc=0) => {
//     return acc - number
// }
// numbersEach(numbers, subEach)
// console.log(numbersEach(numbers, subEach))

// //곱한다
// const mulEach = (number, acc=1) => {
//     return acc *number
// }
// numbersEach(numbers, mulEach)
// console.log(numbersEach(numbers, mulEach))
//////////////////////////////////////////////////////////////   222       ////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////   333333       ////////////////////////////////////////////////////////

// numbersEach 이후의 제어를 우리가 함수저의 없이 매번 자유롭게 하려면?
// const NUMBER = [1,2,3,4,5,]
// const numbersEach = (numbers, callback) => {
//     let acc
//     for (let i =0; i<numbers.length; i++){
//         number = numbers[i]
//         acc = callback(number, acc)
//     }
//     return acc
// }
// console.log(numbersEach(NUMBER, (number, acc=0) => acc+number))
// console.log(numbersEach(NUMBER, (number, acc=0) => acc-number))
// console.log(numbersEach(NUMBER, (number, acc=1) => acc*number))
//////////////////////////////////////////////////////////////   333333       ////////////////////////////////////////////////////////