<template>
  <div class="shopcar-container">
        <div class="list-item " v-for="(item,i) in goodslist" data-type="0" :key="item.id">
          <div class="list-box" @touchstart.capture="touchStart" @touchend.capture="touchEnd" >
            <div class="mui-input-row mui-checkbox mui-left">
              <label>&nbsp;</label>
              <input style="top: 15px" type="checkbox" v-model="getGoodsSelected[item.id]"
                     @change="selectedChange(item.id,getGoodsSelected[item.id])"
                     :disabled="item.num == 0">
            </div>
            <img class="list-img" :src="item.image" alt="">
            <div class="list-content">
              <span class="name">{{item.name}}</span>
              <p class="num"><numbox v-if="item.num" @count="countChange" :max="item.num"
                                                    :goodsid="item.id" :initcount="getGoodsCount[item.id]" size="min"></numbox>
                <numbox v-else style="margin-right: 20px">该商品暂时缺货</numbox></p>
              <p class="time" style="color: #2ac845;font-size: 14px">￥{{item.price/2}}</p>
            </div>
          </div>
          <div class="delete" @click.prevent="remove(item.id,i)"><p>删除</p></div>
        </div>

      <!--结算信息-->
      <div class="footer">
       <div class="mui-card">
         <div class="mui-card-content">
           <div class="mui-card-content-inner balance">
             <div class="left">
               <!--<p>总计不算运费</p>-->
               <p>已勾选游戏<span class="red">{{getSelectedCount}}</span>件,总价
               <span class="red">{{getSelectedAmount/2}}</span> </p>
             </div>
             <mt-button type="danger" @click="createOrder">去结算</mt-button>
           </div>
         </div>
       </div>
    </div>
    </div>

</template>

<script>
  import {mapState,mapGetters} from 'vuex'
  import numbox from '../components/numbox.vue'
  export default {
    name: "Shopcart",
    data(){
      return{
        goodslist:[],

        startX: 0,
        endX: 0,
      }
    },
    computed:{
      ...mapState('shopcart',['car']),
      //将shopcart modules中的getters中的'getGoodsCount','getGoodsSelected','getSelectedGoods','getSelectdCount'引入到当前组件
      ...mapGetters('shopcart',['getGoodsCount','getGoodsSelected','getSelectedGoods','getSelectedCount']),
      //获得被选中商品的总价
      getSelectedAmount()
      {
        //获得了所有被选中的商品放到goods变量中
        var goods=this.getSelectedGoods;
        var amount=0;//总价
        //this.goodslist是当前购物车列表
        this.goodslist.forEach(item=>{
          if(goods[item.id])//是否为选中商品
          {
            amount+=item.price*goods[item.id].count;//单价*数量
          }
        })
        return amount;
      }
    },
    components:{
      numbox
    },
    created(){
      this.getgoodsList();
    },
    methods:{

      //滑动开始
      touchStart:function(e) {
        // 记录初始位置
        this.startX = e.touches[0].clientX;
      },
      //滑动结束
      touchEnd:function(e) {
        // 当前滑动的父级元素
        let parentElement = e.currentTarget.parentElement;
        // 记录结束位置
        this.endX = e.changedTouches[0].clientX;
        // 左滑
        if(parentElement.dataset.type == 0 && this.startX - this.endX > 30) {
          this.restSlide();
          parentElement.dataset.type = 1;
        }
        // 右滑
        if(parentElement.dataset.type == 1 && this.startX - this.endX < -30) {
          this.restSlide();
          parentElement.dataset.type = 0;
        }
        this.startX = 0;
        this.endX = 0;
      },
      //判断当前是否有滑块处于滑动状态
      checkSlide:function() {
        let listItems = document.querySelectorAll('.list-item');
        for(let i = 0; i < listItems.length; i++) {
          if(listItems[i].dataset.type == 1) {
            return true;
          }
        }
        return false;
      },
      //复位滑动状态
      restSlide:function() {
        let listItems = document.querySelectorAll('.list-item');
        // 复位
        for(let i = 0; i < listItems.length; i++) {
          listItems[i].dataset.type = 0;
        }
      },

      getgoodsList(){
        var idArr=[];
        this.car.forEach(item=>{
          idArr.push(item.id)
        });
        if (idArr.length<=0){
          return;
        }

        this.$indicator.open({
          text:"加载中ing",

        });
        var params={ids:idArr};
        this.$http.get('shopcart',{params:params}).then(res=>{
          this.$indicator.close();
          if (res.data.code===1)
          {
            this.goodslist=res.data.data;
            this.goodslist.forEach(item=>{
              //商品无货
              if(item.num==0)
              {
                this.selectedChange(item.id,false);
              }
            })
          }
        })
      },
      //修改商品数量
      countChange(goodsinfo)
      {
        this.$store.commit('shopcart/updateGoodsInfo',goodsinfo);
      },
      //修改商品选中状态
      //参数1是商品id，参数2是选中状态
      selectedChange(id,val)
      {
        this.$store.commit('shopcart/updateGoodsSelected',{id:id,selected:val})
      },
      remove(id,index)
      {
        this.goodslist.splice(index,1);
        this.$store.commit('shopcart/removeCar',id)
      },
      //创建订单
      createOrder()
      {
        if(this.goodslist.length ===0){
          this.$toast('您的购物车为空');
          return
        }
        this.$store.commit('shopcart/setBuy');
        this.$router.push({name:'order_create'});//页面跳转
      }
    }
  }
</script>

<style lang="scss" scoped>
  .flex {
    display: flex;
  }
  .shopcar-container {
    background: #eee;
    overflow: hidden;
    .goods-list {
      .mui-card-content-inner {
        align-items: center;
        padding: 10px;
        .mui-checkbox.mui-left input[type="checkbox"] {
          left: 0px;
        }
        .mui-radio.mui-left label,
        .mui-checkbox.mui-left label {
          padding-left: 20px;
          padding-right: 35px;
          padding-bottom: 22px;
        }
      }
      img {
        width: 60px;
      }
      .info {
        margin-left: 10px;
        width: 100%;
        overflow: hidden;
        box-sizing: border-box;
        h1 {
          font-size: 13px;
          font-weight: bold;
          line-height: 20px;
          padding-top: 10px;
        }
        p {
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: space-between;
          .price {
            text-align: left;
            font-size: 16px;
            font-weight: 700;
            color: red;
            flex: 1;
          }
          a {
            line-height: 25px;
          }
        }
      }
    }
    .balance {
      display: flex;
      justify-content: space-between;
      align-items: center;
      .red {
        color: #2ac845;
        font-weight: bold;
        font-size: 16px;
      }
    }
  }
  .footer{
    width: 100%;
    position: fixed;
    bottom: 50px;
  }

</style>

<style type="text/css">

  .page-title {
    text-align: center;
    font-size: 0.85rem;
    padding: 0.5rem 0.75rem;
    position: relative;
  }

  .list-item {
    position: relative;
    height: 6rem;
     -webkit-transition: all 0.2s;
    transition: all 0.2s;
    background: linear-gradient(90deg,#282A32,#233E40);
  }

  .list-item[data-type="0"] {
    transform: translate3d(0, 0, 0);
  }

  .list-item[data-type="1"] {
    transform: translate3d(-5rem, 0, 0);
  }

  .list-box {
    padding: 0.5rem;
    background: #16202D;
    display: flex;
    /*align-items: center;*/
     /*-webkit-box-sizing: border-box;*/
    /*box-sizing: border-box;*/
    /*justify-content: flex-end;*/
    /*font-size: 0;*/
  }

  .list-item .list-img {
    display: block;
    width: 4.5rem;
    height: 4.5rem;
  }

  .list-item .list-content {
    padding: 0.25rem 0 0.25rem 0.5rem;
    position: relative;
    flex: 1;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    overflow: hidden;
  }

  .list-item .name {
    display: block;
    color: white;
    overflow: hidden;
    font-size: 16px;
    font-weight: bold;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-right: 20px;
  }

  .list-item .num {
    display: block;
    overflow: hidden;
    font-size: 0.6rem;
    color: #999;
    line-height: 1rem;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-top: 10px;
    margin-right: 20px;
  }

  .list-item .time {
    display: block;
    font-size: 0.6rem;
    position: absolute;
    right: 0;
    top: 0.25rem;
    color: red;
    margin-top: 30px;
  }

  .list-item .delete {
    width: 5rem;
    height: 96px;
    background: #ff4949;
    font-size: 1rem;
    color: #fff;
    text-align: center;
    line-height: 4rem;
    position: absolute;
    top: 0;
    right: -5rem;
  }
  .list-item .delete p{
    height: 96px;
    color: white;
    margin-top: 15px;
    font-size: 15px;
  }

</style>
