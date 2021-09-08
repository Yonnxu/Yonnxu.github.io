<template>
    <div class="tab-bar-item" @click="itemClick">

        <div v-if="!isActive">
            <slot name="item-icon"></slot>
        </div>

        <div v-else>
            <slot name="item-icon-active"></slot>
        </div>

<!--         动态绑定活跃状态的颜色-->
        <div :style="activeStyle">
            <slot name="item-text"></slot>
        </div>

    </div>
</template>

<script>
    export default {
        name: "TabBarItem",
        props: {
            path: String,
            activeColor:{
                Type:String,
                // 默认为红色
                default:'deeppink'
            }
        },
        data() {
            return {}
        },
        computed: {
            isActive() {
                // indexOf没有找到传入的值输出为-1
                return this.$route.path.indexOf(this.path) !== -1
            },
            activeStyle(){
                // 首先查看是否属于活跃 再进行三元运算符
                return this.isActive ? {color:this.activeColor} :{}
            }
        },
        methods: {
            itemClick() {
                this.$router.push(this.path)
            }
        }
    }
</script>

<style scoped>
    .tab-bar-item {
        flex: 1;
        text-align: center;
        height: 49px;
        font-size: 14px;
    }

    .tab-bar-item img {
        width: 24px;
        height: 24px;
        margin-top: 3px;
        vertical-align: middle;
        margin-bottom: 2px;
    }

</style>