import axios from 'axios'
import config from './config'

export default {
  install:function (vue) {
    //从vue的原生链中获取$auth,赋给auth变量
    var auth=vue.prototype.$auth;
    var obj=axios.create({
      baseURL:config.baseURL
    })
    //interceptors是拦截器
    obj.interceptors.request.use(function (conf)
    {
      conf.headers.Authorization=auth.getAuthorization();
      return conf;
    })
    //prototype:jis的原生链,可以是继承
    //vue.prototype.$http=obj,通过原生链为vue添加属性或者方法
    //所有的vue对象就都可以拥有这些属性和方法
    vue.prototype.$http=obj
  }
}
