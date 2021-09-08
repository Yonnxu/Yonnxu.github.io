const state={
  id:0,
  username:''
}
//对state数据进行包装，再抛出
const getters={
  isLogin(state)
  {
    return state.id!== 0  //不等于0，返回true
  }
}
const actions={

}

const mutations={
  setUser(state,user)
  {
    state.id=user.id;
    state.username=user.username
  },
  logout(state)
  {
    state.id=0;
    state.username='';
  }
}

export default{
  namespaced:true,
  state,
  getters,
  actions,
  mutations
}
