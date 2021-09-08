<template>
    <div class="goods-info">
        <div class="mui-card">
            <div class="mui-card-content">
                <!--<div class="mui-card-content-inner">-->
                  <!--<swiper :images-list="goodsinfo.album"></swiper>-->
                <!--</div>-->
              <swiper :img-list="goodsinfo.album"></swiper>
            </div>
                </div>
        <div class="mui-card">

            <div class="mui-card-header">
                {{goodsinfo.name}}
            </div>
            <div class="mui-card-content">
                <div class="mui-card-content-inner">
                    <p class="price">
                        原价<span style="text-decoration:line-through">￥{{goodsinfo.price}}</span>
                    </p>
                  <p class="price">
                    现价<span style="color: #2ac845">￥{{goodsinfo.price/2}}</span>
                  </p>
                    <p class="go-num">
                        <numbox @count="countChange" :max="goodsinfo.num" initcount="1" :goodsid="goodsinfo.id"></numbox>
                    </p>
                    <div v-if="goodsinfo.num">
                        <p class="go-buy">
                            <mt-button type="primary" size="small" @click="buy">立即购买</mt-button>
                            <mt-button type="danger" size="small" @click="addShopcart">加入购物车</mt-button>
                        </p>
                    </div>
                    <div v-else>商品暂时无货</div>
                </div>
            </div>
        </div>
        <div class="mui-card">
            <div class="mui-card-header">商品参数</div>
            <div class="mui-card-content">
                <div class="mui-card-content-inner">
                    <p>库存情况:{{goodsinfo.num}}</p>
                    <p>上架时间:{{goodsinfo.create_time}}</p>
                </div>
            </div>
            <div class="mui-card-header">商品详情</div>
            <div class="good-desc">
                <div class="content" v-html="goodsinfo.content"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import swiper from "../../components/swiper.vue";
    import numbox from "../../components/numbox.vue";
    // import goods from "../../../../shopping/src/store/modules/goods";

    export default {
        name: "GoodsInfo",
        props: ['id'],
        components:{
            swiper,
            numbox
        },
        data() {
            return {
                goodsinfo: {},//商品对象
              selectedCount:1,//商品数量

            }
        },
        created() {
            this.getGoodsInfo();
        },
        methods: {
            getGoodsInfo() {
                this.$indicator.open({
                    text: '加载中'
                });
                let params = {id: this.id};
                this.$http.get('goodsinfo', {params:params}).then(res => {
                    this.$indicator.close();
                    if (res.data.code === 0)// 网络访问成功，数据返回失败
                    {
                        this.$toast(res.data.msg)
                    } else if (res.data.code === 1)// 访问成功
                    {
                        if (res.data.data) {
                            this.goodsinfo = res.data.data;
                        } else {
                            // 先提示商品不存在，跳转到前一个页面(商品列表页面)
                            this.$messagebox.alert('商品不存在').then(() => {
                                this.$router.go(-1);
                            })
                        }

                    } else {
                        this.$toast('加载失败，服务器异常')
                    }
                })
            },
            countChange(obj)
            {
                this.selectedCount=obj.count
            },
          //加入购物车
          //加入购物车的对象包含3个属性：id,
          addShopcart()
          {
            this.$store.commit('shopcart/addCar',{
              id:this.id,
              count:this.selectedCount,
              selected:true
            })
            this.$router.push({name:'shopcart'})
          },
          buy(){
              this.$store.commit('shopcart/setBuy',{
                id:this.$props.id,count:this.selectedCount
              })
              this.$router.push({name:'order_create'})
          }
        }
    }
</script>

<style lang="scss" scoped>
    .goods-info {
      background: linear-gradient(90deg,#282A32,#233E40);
        overflow: hidden;

        .price {
            span {
                color: red;
                font-size: 14px;
                font-weight: bold;
            }
        }

        .go-buy {
            display: flex;
            margin: 10px 0 0px;
            justify-content: center;

            button {
                margin: 0 5px;
            }
        }

        .good-desc {
            background: #262627;
            padding: 5px;

            h3 {
                font-size: 16px;
                color: #226aff;
                text-align: center;
                margin: 15px 0;
            }

            .content {
                font-size: 14px;
                line-height: 28px;
                img {
                    width: 100%;
                }
            }
        }

        .go-num {
            div {
                margin-left: 10px;
            }
        }

        .ball {
            width: 15px;
            height: 15px;
            border-radius: 50%;
            position: absolute;
            background: red;
            z-index: 99;
            left: 132px;
            top: 390px;
            transform: translate(93px, 230px);
        }
    }
</style>
