const state={
  car:getItem('car'),
  buy:getItem('buy')//当前准备购买的商品信息
};

const getters={
  getGoodsCount(state){
    var goods={};
    state.car.forEach(item=>{
      goods[item.id]=item.count;
    });
    return goods;
   },
  //获取商品是否被选中的状态值
  getGoodsSelected(state){
    var goods={};
    state.car.forEach(item=>{
      goods[item.id]=item.selected
    });
    return goods;
  },
  getSelectedCount(state){
    var count=0;
    state.car.forEach(item=>{
      if (item.selected){
        count+=item.count;
      }
    });
    return count;
  },
  getSelectedGoods(state){
    var goods={};
    state.car.forEach(item=>{
      if (item.selected){
        goods[item.id]=item;
      }
    });
    return goods;
  },
  //获得要购买的商品
  getBuy(state) {
    var goods = {};
    state.buy.forEach(item => {
      goods[item.id] = item;
    });
    return goods;
  }
};

const actions={};

const mutations={
  addCar(state,goodsinfo){
    var flag=false;
    state.car.some(item=>{
      if (item.id===goodsinfo.id){
        item.count+=parseInt(goodsinfo.count);
        flag=true;
        return true;
      }
    });
    if (!flag){
      state.car.push(goodsinfo);//商品不在购物车中
    }
    //将car重新保存到localStorage中
    setItem('car',state.car)
  },
  //购买数量的加减
  updateGoodsInfo(state,goodsInfo)
  {
    state.car.some(item=>{
      if(item.id === goodsInfo.id) {
        item.count = parseInt(goodsInfo.count);
        return true;
      }
    })
    setItem('car',state.car);
  },
  //修改选中状态
  updateGoodsSelected(state,info)
  {
    state.car.some(item=>{
      if(item.id === info.id){
        item.selected=info.selected;
        return true;
      }
    })
     setItem('car',state.car);
  },
  removeCar(state,id)
  {
    state.car.some((item, i)=> {
      if (item.id === id) {
        state.car.splice(i,1)
        return true;
      }
    })
    setItem('car', state.car);
  },
  //将购物车中用户选择的商品设置为要购买的商品，保存下来
  setBuy(state,goods)
  {
    state.buy=[];
    if(goods){
      state.buy.push(goods)
    }else {
      state.car.some(item=>{
        if(item.selected){
          state.buy.push(item)
        }
      })
    }
    setItem('buy',state.buy)
    //car是数组，some进行搜索
    state.car.some(item=>{
      if(item.selected)
      {
        state.buy.push(item);
      }
    })
    setItem('buy',state.buy);
  }
};

function setItem(name,item)
{
  //将item转换成JSON字符串后，保存到本地的localStorage中
    localStorage.setItem(name,JSON.stringify(item));
}

function getItem ()
{
  //JSON.parse 将JSON字符串转换成JSON对象
  //||表示初始情况
  return JSON.parse(localStorage.getItem(name) || '[]')
}

export default {
  namespaced:true,
  state,
  getters,
  actions,
  mutations
}
