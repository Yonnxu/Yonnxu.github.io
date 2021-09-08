<template>
    <div id="box">

        <input type="search" name="search" placeholder="请输入关键字" :input="searchValueInput" value="{{searchValue}}">

        <div id="search" @click="searchs">搜索</div>
    </div>

    <div>
        <swiper :imgList="imgList"></swiper>
    </div>
    <div class="mui-card">
        <div class="mui-card-content" v-for="(item,i) in searchValueInput" :key="item.id">
            <div class="mui-card-content-inner flex">
                <div class="mui-input-row mui-checkbox mui-left">
                    <label>&nbsp;</label>
                    <input type="checkbox" v-model="getGoodsSelected[item.id]"
                           @change="selectedChange(item.id,getGoodsSelected[item.id])"
                           :disabled="item.num == 0">
                </div>
                <img :src="item.image">
                <div class="info">

                    <p style="font-size: 20px;margin-top: 10px;margin-left: 10px;">{{item.name}}</p>

                    <p class="flex">
                        <span class="price">￥{{item.price}}</span>
                        <numbox v-if="item.num" @count="countChange" :max="item.num"
                                :goodsid="item.id" :initcount="getGoodsCount[item.id]" size="min"></numbox>
                        <numbox v-else style="margin-right: 20px">该商品暂时缺货</numbox>
                        <a href="#" @click.prevent="remove(item.id,i)" style="margin-left: 5px">删除</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Swiper from '../components/swiper'
    export default {
        name: "search",

        components: {
            Swiper
        },
        data(){
          return{
              imgList:[],
              searchValueInput:[]
          }
        },
        methods:{
            searchs(){
                this.$indicator.open({
                    text:"加载中"
                });
                this.$http.get('search',{params:params}).then(res=>{
                    this.$indicator.close();
                    if (res.data.code===1)
                    {
                        goodslist=res.data.data;
                        this.goodslist.forEach(item=>{
                            //商品无货
                            if(this.searchValueInput===item.name)
                            {
                                searchValueInput=res.data.data;
                            }
                        })
                    }
                })

            },
            show(){

            }
        }
    }


</script>


<style scoped>
    #box{

        width: 380px;

        margin: 30px auto;

        font-size: 14px;

    }

    input{

        width: 260px;

        border: 1px solid #e2e2e2;

        height: 30px;

        float: left;

        background-image: url(../assets/images/avatar_default.png);

        background-repeat: no-repeat;

        background-size: 25px;

        background-position:5px center;

        padding:0 0 0 40px;

    }

    #search{

        width: 78px;

        height: 32px;

        float: right;

        background: black;

        color: white;

        text-align: center;

        line-height: 32px;

        cursor: pointer;

    }
</style>
