// Little people
function f() {
    L2Dwidget.init({
        model: {jsonPath: "live2d/live2dw/assets/asuna_04.model.json"}
    })
}

f();

// Dom加载完成，移除Loading

$(function(){
    $(".loading").remove()
});
    // 监听加载状态改变
    // document.onreadystatechange = completeLoading;
    // console.log(document.readyState)
    // // 加载状态为complete时移除loading效果
    // function completeLoading() {
    //     if (document.readyState === "complete") {
    //         var loadingMask = document.getElementById('svg');
    //         loadingMask.parentNode.removeChild(loadingMask);
    //         console.log(document.readyState)
    //     }
    // }
// }
// Dynamic Title
window.onfocus = function () {
    document.title = 'Administratorの博客 ~(@^_^@)~...';
};
window.onblur = function () {
    document.title = '快回来~页面崩溃了 ┭┮﹏┭┮';
};

