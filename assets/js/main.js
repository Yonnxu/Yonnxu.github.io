// Little people
function f() {
    L2Dwidget.init({
        model: {jsonPath: "live2d/live2dw/assets/asuna_04.model.json"}
    })
}

f();

// Dom加载完成，移除Loading

$(function(){
    $(".loadings").remove()
});

// Dynamic Title
window.onfocus = function () {
    document.title = 'Administrator';
};
window.onblur = function () {
    document.title = '快回来~页面崩溃了 ┭┮﹏┭┮';
};

