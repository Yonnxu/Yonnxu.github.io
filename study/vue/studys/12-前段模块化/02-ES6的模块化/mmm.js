// 1.导入的{}中定义的变量
import {flag,sum} from "./aaa.js"
if(flag){
    console.log('小明天才');
    console.log(sum(20,30))
}

// 2.直接导入export定义的变量
import {num1,height} from "./aaa.js";

console.log(num1);
console.log(height);

// 3.导出export的function
import {mul,Person} from './aaa.js';

console.log(mul(30, 50));
const p=new Person();
p.run();

// 4.导入export default中的内容
import add from './aaa.js'

// console.log(add);
add('hello');

// 5.统一全部导入
import * as aaa from './aaa.js'

console.log(aaa.flag);
console.log(aaa.height);

