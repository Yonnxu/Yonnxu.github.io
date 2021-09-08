<template>
    <div class="mui-numbox" data-numbox-min="1" :data-numbox-max="max" :style="myStyle">
        <button class="mui-btn mui-btn-numbox-minus" type="button">-</button>
        <input class="mui-input-numbox" type="number" :value="initcount" @change="countChanged" ref="num">
        <button class="mui-btn mui-btn-numbox-plus" type="button">+</button>


    </div>
</template>

<script>
    import mui from '../lib/mui/js/mui.min.js'
    export default {
        name: "numbox",
        data(){
          return{
            myStyle:[]
          }
        },
        mounted() {
            //创建class='mui-numbox'的numbox。
            mui('.mui-numbox').numbox();
            if(this.$props.size=='min')
            {
              this.myStyle={height:'25px',magin:'0 5px 0px 10px'}
            }
        },
        methods:{
            countChanged(){
                var count=parseInt(this.$refs.num.value);
                // 子传父
                this.$emit('count',{id:this.goodsid,count:count});// 传参
            }
        },
        props:['initcount','max','goodsid','size'], // 父传子
        watch:{
            // 发送变化把新值给newVal
            'max'(newVal){
                mui('.mui-numbox').numbox().setOption('max',newVal);

            }
        }
    }
</script>

<style scoped>

</style>
