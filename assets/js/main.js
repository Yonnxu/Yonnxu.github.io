// Little people
function f() {
    L2Dwidget.init({
        model: {jsonPath: "live2d/live2dw/assets/asuna_04.model.json"}
    })
}

f();

// Dom加载完成，移除Loading

$(function(){
    $(".loadings").fadeTo("slow", 0.2, function(){
            $(".loadings").remove();
    });
    $(".gtr-25 div").hover(function () {
        $(this).siblings().stop().fadeTo(1000,0.5)
    },function () {
        $(this).siblings().stop().fadeTo(1000,1)
    })
});



// Dynamic Title
window.onfocus = function () {
    document.title = 'Administrator';
};
window.onblur = function () {
    document.title = '快回来~页面崩溃了 ┭┮﹏┭┮';
};

