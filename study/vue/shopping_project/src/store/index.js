import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import shopcart from './modules/shopcart'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isShow:false,
    // menus:[],
    // rightHeight:[],//右边菜单每一项的高度
    // scrollY:0//记住右菜单的滚动距离
  },
  mutations: {
    showBar(state){
      state.isShow=true;
    },
    hideBar(state){
      state.isShow=false;
    }
  },
  actions: {
    showSideBar({commit}){
      commit('showBar')
    },
    hideSideBar({commit}){
      commit('hideBar')
    }
  },
  modules: {
    user,
    shopcart
  },
  getters:{
    isShowMethod(state){
      return state.isShow;
    }
  }
})
