// 1. forEach
// 아무것도 리턴하지 않는다.
// ES5 방식
// var color = ['red','blue','green',]

// for (var i=0; i< color.length; i++){
//     console.log(color[i])
// }

// //  ES6방식
// var COLOR = ['red','blue','green',]

// COLOR.forEach(function (color){
//     console.log(color)
// })
// COLOR.forEach( color => console.log(color)) //는 arrow function

//====================================================================================
// 1-1 아래 함수에 for를 forEach로 바꾸시오
// function handlePosts() {
//     const posts = [
//         { id:23, title:'daily news'},
//         { id:52, title:'Code City'},
//         { id:105, title:'The ruby'},
//     ]
//     // for (let i =0; i<posts.length; i++){
//         savePost(post)
//     }
//     posts.forEach(function (MMM){
//         // console.log(MMM)
//         savePost(MMM)
//     })
// handlePosts()

// //====================================================================================
// //====================================================================================
// //1-2 아래 코드의 image배열안에 있는 정보를 곱ㅎ ㅐ넓이를 구하여 areas 배열에 저장하는 코드를 forEach를 사용해 작성해보자
// const images = [
//     { height:10, width:30},
//     { height:20, width:90},
//     { height:54, width:32},
// ]
// const aresa = []

// images.forEach(function (image) {
//     aresa.push(image.height * image.width)
// })
// console.log(aresa)

//======================================================================================================
//======================================================================================================
//======================================================================================================
//======================================================================================================

// 2. map
    // map 함수는 새로운 배열을 return한다.(배열 요소를 변형)
    // 일정한 형식의 배열을 다른 형식으로 바꿔야할때,
    // map filter는 모두 사본을 return하며 원본은 바뀌지 않는다.
// const NUMBERS = [1,2,3,]

// const DOUBLE_NUMBERS = NUMBERS.map(function (number){
//     return number * 2
// // })
// const DOUBLE_NUMBERS = NUMBERS.map(number=> number * 2)
// console.log(DOUBLE_NUMBERS)

// = = = =  = =  = = = = = = = = =  = = = =  = = =  = = == = = = = = =
// = = = =  = =  = = = = = = = = =  = = = =  = = =  = = == = = = = = =
// = = = =  = =  = = = = = = = = =  = = = =  = = =  = = == = = = = = =

// 2-1 map을 이용해 images.배열안의 object만 저장되잇는 height만 저장되어있는 heights배열에 저장해보자
// const images = [
//     { height:'34px', width:'39px'},
//     { height:'54px', width:'19px'},
//     { height:'83px', width:'75px'},
// ]
// const heights = []

// images.map(function (image){
//     heights.push(image['height'])
// })

// console.log(heights)
// // =========================================================

// // 2-2 map을 이용해 distance / time을 저장하는 배열 speeds를 마늗ㄹ어보자
// const trips = [
//     { distance:34, time:10 },
//     { distance:90, time:50 },
//     { distance:59, time:25 },
// ]

// // const speeds = []
// // trips.map(function (trip){
// //     speeds.push(trip['distance']/trip['time'])
// // })
// const speeds = trips.map(function (trip){
//     return (trip['distance']/trip['time'])
// })
// console.log(speeds)

// // 2-3 다음 두 배열을 객체로 결합한 comics 배열을 만들어보자(brands 요소가 key, moview요소가 value) 힌트 : enumerate

// const brands = ["Marvel", "DC"]
// const movies = ["IronMan", "BatMan"]

// const comics = brands.map((x,i) => ({name: x, hero:movies[i]}))
// console.log(comics)

// ===================================================================================================================
// ===================================================================================================================
// ===================================================================================================================
// ===================================================================================================================

// 3. filter
// filter함수는 필터링 된 요소들만 배열로 return 한다.
// 배열에서 필욯나 것들만 남길때 사용한다.
// const PRODUCTS = [
//     { name: 'cucumber', type: 'vegetable' },
//     { name: 'banana', type: 'fruit' },
//     { name: 'carrot', type: 'vegetable' },
//     { name: 'apple', type: 'fruit' },
//  ]
// //  const fruitProducts = PRODUCTS.filter(function (MMMMM){
// //      return MMMMM.type === 'fruit'
// //      // 해당 조건문에서 true를 만족할 경우 return
// //  })
//  const fruitProducts = PRODUCTS.filter(MMMMM => MMMMM.type === 'fruit')
//     // 해당 조건문에서 true를 만족할 경우 return

//  console.log(fruitProducts)

// // 3-1 filter 헬퍼를 사용해서, numbers 배열 중 50보다 큰 값들만 필터링해서 filteredNumbers 에 저장하라.
// const numbers = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]
// const filteredNumbers = numbers.filter(function (number){
//     return number > 50
// })
// console.log(filteredNumbers)

// // 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.
// const users = [
//     {id: 1, admin: true},
//     {id: 2, admin: false},
//     {id: 3, admin: false},
//     {id: 4, admin: false},
//     {id: 5, admin: true},
// ]
// const filteredUsers = users.filter(function (user){
//     return user.admin === true
// })
// console.log(filteredUsers)