import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../pages/Home.vue'
import Category from '../pages/Category.vue'
import Shopcart from '../pages/Shopcart.vue'
// import User from '../pages/User.vue'
import Login from '../pages/user/Login.vue'
import Register from '../pages/user/Register.vue'
import GoodsList from '../pages/goods/GoodsList.vue'
import GoodsInfo from '../pages/goods/GoodsInfo.vue'
import Address from '../pages/user/Address.vue'
import AddressEdit from '../pages/user/AddressEdit.vue'
import OrderCreate from '../pages/order/OrderCreate.vue'
import OrderList from '@/pages/order/OrderList.vue'
import OrderShow from '@/pages/order/OrderShow.vue'
import NewsList from  '../pages/news/NewsList.vue'
import NewsInfo from '../pages/news/NewsInfo.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/category',
    meta:{
      title:"游戏PY交易商城"
    }
  },
  // {
  //   path: '/home',
  //   component:Home,
  //     name:'home',
  //     meta:{
  //     title:'首页'
  //     }
  // },
    {
        path: '/category',
        component:Category,
        name:'category',
        meta:{
            title:'游戏PY交易商城'
        }
    },
    {
        path: '/shopcart',
        component:Shopcart,
        name:'shopcart',
        meta:{
            title:'购物车'
        }
    },
    {
        path: '/user/login',
        component:Login,
        name:'login',
        meta:{
            title:'登录'
        }
    },
    {
        path: '/goodslist/:category_id',
        component:GoodsList,
        name:'goods_list',
        meta:{
            title:'游戏介绍'
        },
        props:true
    },
  {
    path: '/goodsinfo/:id',
    component: GoodsInfo,
    name: 'goods_info',
    meta: {
      title: '商品信息'
    },
    props: true
  },
    {
        path: '/user/register',
        component:Register,
        name:'register',
        meta:{
            title:'注册'
        }
    },
  {
    path:'/user/address',
    component:Address,
    name:'address',
    meta:{
      title:'收货地址'
    },
    props: true
  },
  {
    path: '/user/address/add',
    component: AddressEdit,
    name: 'address_add',
    meta: {
      title: '新增收货地址'
    },
    props: true
  },
  {
    path: '/user/address/edit/:id',
    component: AddressEdit,
    name: 'address_edit',
    meta: {
      title: '编辑收货地址'
    },
    props: true
  },
  {
    path: '/order/create',
    component: OrderCreate,
    name: 'order_create',
    meta: {
      title: '下订单'
    }
  },
    { path: '/order/list',
        component: OrderList,
        name: 'order_list',
        meta: { title: '我的订单' } },
    {path:'/order/show/:id',
        component:OrderShow,
        props:true,
        name:'order_show',
        meta:{title:'查看订单'}
    },
    {path:'/user/address/select',
        component:Address,name:'address_select',
        meta:{title:'选择收货地址'}
        },
  {
    path:'/news/list',
    component:NewsList,
    name:'news_list',
    meta:{
      title:'游戏资讯列表'
    }
  },
  {
    path:'/news/show/:id',
    component:NewsInfo,
    props:true,
    name:'news_show',
    meta:{
      title:'查看游戏资讯'
    }
  }

]

const router = new VueRouter({
  routes,
    linkActiveClass:'mui-active'//激活样式
})

//路由管理者的钩子函数
//to:表示即将进入的目标路由器对象
//from:当前即将离开的路由对象
//next:函数，要保证next函数被调用
router.beforeEach((to,from,next)=>{
  if (to.meta.title){
      document.title=to.meta.title;
  }
  next()
})

export default router
