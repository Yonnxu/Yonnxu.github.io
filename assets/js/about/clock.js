
function myTime(){
  const time = new Date();
  const hh = time.getHours();
  const mm = time.getMinutes();
  const ss = time.getSeconds();
  //这里用const可以不用去判断作用域,比用let和var的性能要好

  document.getElementById('clock').innerText = Math.floor(hh / 10) + (hh % 10 + ':') + Math.floor(mm / 10) + mm % 10 + ':' + Math.floor(ss / 10) + ss % 10;
  //因为js的/不是整除而是会求出浮点数
  //所以这里要用Math.floor()方法来向下取整
}
myTime();
setInterval(myTime, 1000);

// function f() {
//   const time = new Date();
//   const hh = time.getHours();
//
//   if(parseInt(Math.floor(hh / 10).toString()+(hh % 10).toString())>=22||parseInt(Math.floor(hh / 10).toString()+(hh % 10).toString())<6){
//     document.body.classList.add('night');
//     document.cookie = "night=1;path=/";
//     console.log(Math.floor(hh / 10).toString()+(hh % 10).toString())
//   }else{
//     document.body.classList.remove('night');
//     document.cookie = "night=0;path=/";
//     console.log('夜间模式关闭');
//     console.log(Math.floor(hh / 10).toString()+(hh % 10).toString())
//   }
// }
// f()