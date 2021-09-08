<template>
    <div class="goods-list">
        <div class="goods-item" v-for="item in goodslist" :key="item.id">
                <img :src="item.image">
                <h1 class="title">{{item.name}}</h1>
          <div class="mui-card-header" style="color: #1c7430;">游戏特点:</div>

              <P class="title" style="font-size: 16px;color:dodgerblue">{{item.sell_point}}</P>
                <p class="info">
                    <span class="price" style="text-decoration:line-through">￥{{item.price}}</span>
                    <span class="price" style="color: #2ac845">-50%</span>
                </p>
          <p class="info">
            <span class="price" style="color: #2ac845">￥{{item.price/2}}</span>
            <span class="sell">库存:{{item.num}}件</span>
          </p>
          <router-link :to="{name:'goods_info',params:{id: item.id}}">
            <mt-button type="danger" size="small">购买界面</mt-button>
          </router-link>
        </div>
        <!--<mt-button class="more" v-if="goodslist.length!==0" size="large" @click="getMore">-->
            <!--加载更多-->
        <!--</mt-button>-->
    </div>
</template>

<script>
    export default {
        name: "GoodsList",
        props:['category_id'],
        data(){
            return{
                goodslist:[],
                // last_id:0
            }
        },
        //创建组件的钩子函数
        created(){
            this.getGoodsList()
        },
        methods:{
            getGoodsList(){
                this.$indicator.open({
                    text:'加载中'
                });
                let params={category_id:this.category_id,last_id:this.last_id};
                this.$http.get('goodslist',{params:params}).then(res=>{
                    this.$indicator.close();
                    if (res.data.code===1){
                        if (res.data.data.length>0){//有商品
                            //concat将元素加入数组
                            this.goodslist=this.goodslist.concat(res.data.data);
                            // this.last_id=res.data.data[res.data.data.length-1].id
                        }else {
                            this.$toast('列表为空');
                        }
                    }

                })
            },
            getMore(){
                this.getGoodsList()
            }
        }
    }
</script>

<style lang="scss" scoped>
    .goods-list {
        display: flex;
        flex-wrap: wrap;
        padding-left: 10px;
        .goods-item {
            /*width: calc(calc(100% / 2) - 10px);*/
          width: calc(calc(100% / 1) - 10px);
            margin: 10px 10px 0 0;
            background: #282A32;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-radius: 10px;
            padding: 10px;
            img {
                width: 100%;
            }
            .title {
                font-size: 14px;
                color: white;
                margin: 10px 0;
            }
            .info {
                display: flex;
                justify-content: space-between;
                margin-bottom: 0;
                .price {
                    color: red;
                    font-weight: bold;
                    font-size: 16px;
                }
                .sell {
                    font-size: 13px;
                }
            }
        }
        .more {
            margin: 15px 0;
            font-size: 14px;
        }
    }
</style>
