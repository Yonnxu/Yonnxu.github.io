// Little people
function f(){
    L2Dwidget.init({
        model: {jsonPath: "live2d/live2dw/assets/asuna_04.model.json"}
    })

}
f()

// Dynamic Title
window.onfocus = function () {
    document.title = 'Administratorの博客 ~(@^_^@)~...';
};
window.onblur = function () {
    document.title = '快回来~页面崩溃了 ┭┮﹏┭┮';
};

