const app = new Vue({
    el: '#app',
    data: {
        books: [
            {
                id: 1,
                name: '《算法导论》', date: '2006-9', price: 85.00, count: 1
            },
            {
                id: 2,
                name: '《UNIX编程艺术》', date: '2006-2',
                price: 59.00, count: 1
            },
            {
                id: 3,
                name: '《编程珠玑》', date: '2008-10', price: 39.00, count: 1
            },
            {
                id: 4,
                name: '《代码大全》', date: '2006-10', price: 128.00, count: 1
            }
        ]
    },
    methods: {
        // getFinalPrice(price) {
        // return '¥' + price.toFixed(2);
        // },

        // 传入index区分需要修改的书籍 否则无法区分则所有书籍都会改变
        increment(index) {
            this.books[index].count++
        },
        decrement(index) {
            this.books[index].count--
        },
        removeHandle(index) {
            this.books.splice(index, 1)
        }
    },
    computed: {
        totalPrice() {
            // let totalPrice=0;
            // 1.for (let i =0;i<this.books.length;i++){
            //     totalPrice +=this.books[i].price*this.books[i].count
            // }
            // return totalPrice

            // 2.for (let i in this.books)
            // let totalPrice=0;
            // for (let i in this.books){
            //     totalPrice +=this.books[i].price*this.books[i].count
            // }
            // return totalPrice

            // 3.for (let i of this.books)
            let totalPrice = 0;
            for (let item of this.books) {
                totalPrice += item.price * item.count
            }
            return totalPrice

        }
    },
    filters: {
        showPrice(price) {
            return '¥' + price.toFixed(2);
        }
    }
});
// 编程范式:命令式编程/声明式编程
// 编程范式:面向对象编程(第一公民:对象)
// 函数式编程(第一公民:函数)
// 要求：数组内小于100的函数且结果都*2
// filter/map/reduce
// filter中的回调函数有一个要求:必须返回一个boolean值
// true:当返回true时，函数内部会自动将这次回调的n加入到新的数组中
// false：当返回false时，函数内部会过滤这次的n
const nums = [10, 20, 111, 333, 222, 40, 50];

let total = nums.filter(function (n) {
    return n < 100
}).map(function (n) {
    return n * 2
}).reduce(function (preValue, n) {
    return preValue + n
}, 0);
console.log(total);
// // 1.filter函数的使用
// let newNums = nums.filter(function (n) {
//     // 如果为true 会把n加入到新的数组里面 是false则不会
//     return n < 100
// });
// //2.map函数的使用
// let new2Nums=newNums.map(function (n) {
//     return n*2;
// });
// console.log(new2Nums)
// // 3.reduce函数的使用
// // reduce作用对数组中所有的内容进行汇总  proValue是上一次返回的值
// let totle=new2Nums.reduce(function (proValue,n) {
//     return proValue+n;
// },0);
// console.log(totle);
// // 第一个参数是个函数，第二个参数是设置默认值为0，
// // 第一次:prevalue 0n 20
// // 第二次:preValue 20 n 40
// // 第二次:prevalue 60 n 80
// // 第二次:preValue 140 n 100
// // 240
