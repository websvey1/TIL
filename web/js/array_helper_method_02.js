//4. reduce
/*
    -map은 배열의 각 요소를 변형한다면, reduce는 배열 자체를 변형한다
    -배열을 '하나의 값'으로 줄이는 동작(배열의 합, 배열의 평균,)
    -reduce의 첫번째 매개변수는 `누적값(전단계의 결과)==변수` 이다.
    -         두번째 매개변수는 현재배열요소, 현재인덱스, 배열자체 순으로 들어간다.
    */
//    // 4-1 종합
//    const ssafy = [3,9,2,7,]
//    const sum = ssafy.reduce((total,x) => total+x, 0) // 초기값0(=total)
//    console.log(sum)

//    // 4-2 평균
//    const avs = ssafy.reduce((total, x) => total+x, 0)
//    console.log(avs/ssafy.length)

//    // 4-3 초기값 생략
//    // 초기값이 생략되면 누적값은 배열의 첫번째 요소가 초기값이 된다,
//    const sum_2 = ssafy.reduce((total,x) => total+x)

// 5.  find
/*
    - 찾은 요소 1가지만 return 한다(querySelect와 비슷 ?)
    - 조건에 맞는 인덱스가 아니라 요소 자체를 원할때 사용
    - 배열검색 Helper : find, indexOf, lastIndexOf, findIndex, some, every
*/
// const USERS = [
//     { name: 'Thor'},
//     { name: 'Steve Rogers'},
//     { name: 'Tony Stark'},
// ]

// const ironman = USERS.find(function(user){
//     return user.name ==='Tony Stark'
// })
// // ex5버전 같은코드
// for (var i=0; i<USERS.length; i++){
//     if (USERS[i].name === 'Tony Stark'){
//         user = USERS[i]
//         console.log(user)
//         break
//     }
// }
// console.log(ironman)


// // 5-1 users 중에 admin 권한을 가진 요소를 찾아서 admin 에 저장하자.
// const PERSONS = [
//     { id: 1, admin: false },
//     { id: 2, admin: false },
//     { id: 3, admin: true },
//  ]
// const admin = PERSONS.find(function(pick){
//     // return pick.admin === true
//     return pick.admin
// })
// console.log(admin)


// // 5-2 accounts 중에서 잔액이 12 인 object 를 account 에 저장하자.
// const ACCOUNTS = [
//     { balance: -10 },
//     { balance: 12 },
//     { balance: 0 }
// ]
// const ho = ACCOUNTS.find(function(account){
//     return account.balance === 12
// })
// console.log(ho)


// 6. some & every
/*
    - 조건에 대해 boolean값을 ruturn
    - some : 조건에 맞는 요소를 찾으면 검색을 멈추고 true를 return, 찾지못하면 false 
    - every : 해당배열의 모든 요소가 조건에 맞아야 true, 그렇지 않다면 false
            == 조건에 맞지않는 요소를 찾으면 검색을 멈추고 false
*/
// const arr = [1,2,3]
// const a = arr.some(x => x%2 ===0)
// console.log(a)

// // 6-1 컴퓨터의 램이 16보다 큰 요소가 있는지를 some과 every로 비교
// const COMPUTERS = [
//     { name: 'macbook', ram: 17 },
//     { name: 'gram', ram: 8 },
//     { name: 'series9', ram: 32 },
// ]
// const everyComputer = COMPUTERS.every(function (computer){
//     return computer.ram > 16
// })
// console.log(everyComputer)

// const someComputer = COMPUTERS.some(function (computer){
//     return computer.ram >16
// })
// console.log(someComputer)

// 6-2 USERS 배열에서 모두가 hasSubmitted 인지 아닌지를 hasSubmitted 에 저장하라
/*
const USERS = [
    { id: 21, hasSubmitted: true },
    { id: 33, hasSubmitted: false },
    { id: 712, hasSubmitted: true},
  ]
const user = USERS.every(function (user){
    return user.hasSubmitted 
})
console.log(user)​
*/                           // 왠진 모르겠는데 안됌......  console.log(user)부분
// 6-3 REQUESTS 배열에서 각 요청들 중 status 가 pending 인 요청이 있으면, inProgress 변수에 true 를 저장하라.
// const REQUESTS = [
//     { url: '/photos', status: 'complete' },
//     { url: '/albums', status: 'pending' },
//     { url: '/users', status: 'failed' },
//   ]
// const inProgress = REQUESTS.some(function (request){
//     return request.status === 'pending'
// })
// console.log(inProgress)