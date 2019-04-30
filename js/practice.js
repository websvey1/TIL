var _ = require('lodash');
let list = ['짜장면', '짬뽕', '볶음밥',]
let pick = _.sample(list)
// 로또
let numbers = _.range(1,46)
let catchs = _.sampleSize(numbers, 6)
let menu = {
    짜장면:'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg',
    짬뽕:'http://recipe1.ezmember.co.kr/cache/recipe/2015/08/24/835a29917b3a9f074cb8d1636adeefcf1.jpg',
    볶음밥:'http://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/58d359a9ac359adbc4c7fa2603f2e504.jpg',
}
console.log(`오늘의 메뉴는 ${pick}입니다`)
console.log(menu[pick])
console.log(`오늘의 행운의 번호는 ${catchs}`)


let getMin = (a,b) => {
    if ( a>b) {
        return b;
    } return a
    }

let getMinFromArray = nums => {
    let min = Infinity // python float('inf')
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}
ssafy = [1,2,3,4,5,]
console.log(getMinFromArray(ssafy))