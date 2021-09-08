<template>
  <div id="app" class="container">
    <mt-header id="b" fixed :title="$route.meta.title">
      <span slot="left" @click="goBack" v-show="showBack">
        <mt-button icon="back">返回</mt-button>

      </span>
      <span slot="left" v-show="!showBack">
        <img src="./assets/images/fenlei2.png" @click="showSide" style="width: 20px;height: 20px">

        <side-bar></side-bar>
      </span>
    </mt-header>
    <tabbar></tabbar>
    <transition name="fade">
      <router-view/>
    </transition>
  </div>
</template>

<style lang="scss">

  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    box-sizing: border-box;

  }

  .container{
    padding-top: 40px;
    padding-bottom: 50px;
    overflow-x:hidden ;
  }

  .fade-enter {
    opacity: 0;
    transform: translateX(100%);
  }

  .fade-leave-to {
    opacity: 0;
    transform: translateX(-100%);
    position: absolute;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: all 0.5s ease;
  }

  #b{
    background: linear-gradient(180deg, #1E2630, #171A21);
  }
</style>

<script>
    import tabbar from "./components/tabbar.vue";
    import sideBar from "./pages/sideBar";
    export default {
        components: {
             tabbar,
          sideBar
        },
        data(){
            return{
                showBack:false
            }
        },
        created(){
            this.showBack=this.$route.path!=='/category';
            this.checkLogin()
          //localStorage.clear()
        },
        watch:{
            '$route.path'(newVal){
                this.showBack=newVal!=='/category'
            }
        },
        methods:{
          showSide:function(){
            this.$store.dispatch('showSideBar')
          },
            goBack(){
                this.$router.go(-1)
            },
            checkLogin(){
                this.$indicator.open({
                    text:"加载中"
                })
                this.$http.get('user').then(res=>{
                    if (res.data.code===1){
                        this.$store.commit('user/setUser',res.data.data)
                    }
                    this.$indicator.close()
                })
            }
        }
    }
</script>
