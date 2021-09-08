var auth={
  //获得sessionid
  getAuthorization()
  {
    return localStorage.getItem('authorization')
  },
  //设置sessionid
  setAuthorization(Authorization)
  {
    localStorage.setItem('authorization',Authorization)
  }
}

export default {
  install:function (vue)
  {
       vue.prototype.$auth=auth
  }
}
