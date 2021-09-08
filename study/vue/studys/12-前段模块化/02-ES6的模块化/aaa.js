var name='小明';
var age=18;
var flag=true;

function sum(num1,num2) {
    return num1+num2
}

if (flag){
    console.log(sum(20,30));
}
// 第一种方式:
export {
    flag,
    sum
}
// 第二种方式:
export var num1=1000;
export var height=1.8;

// 导出类/函数：
export function mul(num1,num2) {
    return num1+num2
}

export class Person {
    run(){
        console.log('奔跑')
    }
}

const address='北京';
// export {
//     address
// }

// 不用default 导入就必须要同名，使用default则不需要
// 用default只能使用一个不能是多个
// export default address

export default function (argument) {
    console.log(argument)
}
