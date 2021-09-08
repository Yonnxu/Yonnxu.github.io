<template>
  <div class="shopcart-container">
    <img src="../../assets/images/2wm.jpg" alt="" v-show="imgshow" style="width: 100%">
    <!-- 商品列表 -->
    <div class="goods-list" v-show="!imgshow">
      <!-- 商品列表项区域 -->
      <div class="mui-card">
        <div class="mui-card-content" v-for="(item) in order.user_order_goods" :key="item.id">
          <div class="mui-card-content-inner flex">
            <img :src="item.goods_goods.image" />
            <div class="info">
              <h1 style="color: white">{{ item.goods_goods.name }}</h1>
              <p class="flex">
                <span class="price" style="color: #2ac845">¥{{ item.price/2}}</span>
                <span>x{{ item.count }}</span>
              </p>
            </div>
          </div>
        </div>
        <!-- 订单备注 -->
        <div class="process-info">
          <p>
            <strong>订单备注</strong>
          </p>
          <p>
            <span>{{ order.note }}</span>
          </p>
        </div>
        <!-- 配送信息 -->
        <div class="process-info">
          <p>
            <strong>配送服务</strong>
            <strong>快递运输</strong>
          </p>
          <p>
            <span>中小件送货时间</span>
            <span>工作日、双休日与节假日均可送货</span>
          </p>
        </div>
        <!-- 收货地址 -->
        <div class="process-info">
          <p>
            <strong>收货地址</strong>
          </p>
          <p>
            <span>{{ order.address_name }} {{ order.address_tel }}</span>
          </p>
          <p>
            <span>{{ order.address_area }} {{ order.address_detail }}</span>
          </p>
        </div>
      </div>
    </div>
    <!-- 运费信息 -->
    <ul class="fare-info mui-card" style="background-color:#262627">
      <li class="fare-price flex" style="color: white">
        <span>商品金额</span>
        <span class="red">¥{{ order.price/2}}</span>
      </li>
      <li class="fare-price flex" style="color: white">
        <span>运费</span>
        <span class="red">¥0.00</span>
      </li>
      <li class="fare-price flex" style="color: white">
        <span>
          <strong>总价</strong>
        </span>
        <span class="red">¥{{ order.price/2}}</span>
      </li>
      <!-- 去支付按钮 -->
      <div v-if="order.id && !order.is_cancel" class="flex">
        <button class="mui-btn mui-btn-primary mui-btn-block" @click="zhifu">去支付</button>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      order: {},
      imgshow:false
    }
  },
  props: ['id'],
  created () {
    this.getOrder()
  },
  methods: {
    zhifu(){
      this.imgshow=!this.imgshow
    },
    getOrder () {
      this.$indicator.open({
        text: '加载中'
      })
      this.$http.get('order/show', { id: this.$props.id }).then(res => {
        this.$indicator.close()
        if (res.data.code === 0) {
          this.$toast(res.data.msg)
        } else if (res.data.code === 1) {
          this.order = res.data.data
        } else if (res.data.code === 2) {
          this.$router.push({ name: 'login' })
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.flex {
  display: flex;
}
.shopcart-container {
  background: linear-gradient(90deg,#282A32,#233E40);
  overflow: hidden;
  // 商品列表
  .goods-list {
    margin-top: 10px;
    .mui-card {
      margin: 0;
      .mui-card-content {
        border-bottom: 1px solid #eee;
        .mui-card-content-inner {
          align-items: center;
          padding: 10px;
          img {
            width: 60px;
          }
          .info {
            margin-left: 10px;
            box-sizing: border-box;
            width: 100%;
            overflow: hidden;
            h1 {
              font-size: 13px;
              font-weight: bold;
              line-height: 20px;
              padding-top: 22px;
            }
            p {
              flex-direction: row;
              align-items: center;
              justify-content: space-between;
              .price {
                font-size: 16px;
                font-weight: 700;
                color: red;
                flex: 1;
              }
            }
          }
        }
      }
      // 配送信息
      .process-info {
        background-color: #262627;
        padding: 10px;
        border-bottom: 1px solid #eee;
        p {
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: space-between;
          color: white;
          span {
            color: #999;
          }
        }
      }
    }
  }
  // 运费信息
  .fare-info {
    padding: 10px;
    margin: 10px 0 0 0;
    .fare-price {
      padding: 5px 0;
      display: flex;
      justify-content: space-between;
      .red {
        color: #2ac845;
        font-size: 16px;
      }
    }
  }
}
</style>
