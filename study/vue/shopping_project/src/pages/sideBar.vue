<template>
    <div class="home">
        <!-- 对transition不了接的可以查看vue2.0官方文档的“过渡 & 动画” 链接：https://cn.vuejs.org/v2/guide/transitions.html-->
        <transition name="fade" @touchmove.stop.prevent>
            <!-- 这部分功能主要是关闭侧栏菜单，类似一层遮罩的效果 -->
            <div class="menu-mask" v-show="isRellyShow" @click="hideSide"></div>
        </transition>

        <transition name="slide-fade">
            <!-- 这里才是侧栏代码部分 -->
            <div class="side-content" v-show="isRellyShow">


              <!--已登录-->
              <div v-if="isLogin">
                <div class="member">
                  <div class="header-con">
                    <div class="user-info">
                      <div class="avatar-con">
                        <div class="avatar">
                          <label for="file">
                            <img :src="adatar?adatar:require('../assets/images/10086.jpg')" class="image-info" alt="">
                          </label>
                          <input type="file" id="file" name="" accept="image/gif,image/jpeg,image/jpg,image/png" @change="fileChange" style="display: none">
                        </div>
                      </div>
                      <div class="person-con">
                        <span>{{username}}</span><!--username调用-->
                      </div>
                    </div>
                  </div>
                </div>
                <ul class="mui-table-view mui-table-view-chevron">
                  <li class="mui-table-view-cell mui-media" style="background-color:#171A21">
                    <div class="mui-navigate-right">
                      <router-link :to="{name:'order_list'}">
                        <img class="mui-media-object mui-pull-left" src="../assets/images/21.png"/>
                        <div class="mui-media-body">我的订单</div>
                      </router-link>
                    </div>
                  </li>
                  <li class="mui-table-view-cell mui-media" style="background-color:#171A21">
                    <div class="mui-navigate-right">
                      <router-link :to="{name:'address'}">
                        <img class="mui-media-object mui-pull-left" src="../assets/images/22.png"/>
                        <div class="mui-media-body">收货地址</div>
                      </router-link>
                    </div>
                  </li>
                  <li class="mui-table-view-cell mui-media" style="background-color:#171A21">
                    <div class="mui-navigate-right">
                      <router-link :to="{name:'shopcart'}">
                        <img class="mui-media-object mui-pull-left" src="../assets/images/23.png"/>
                        <div class="mui-media-body">购物车</div>
                      </router-link>
                    </div>
                  </li>
                  <li class="mui-table-view-cell mui-media" style="background-color:#171A21">
                    <div class="mui-navigate-right">
                      <router-link :to="{ name:'news_list'}">
                        <img class="mui-media-object mui-pull-left" src="../assets/images/zixun.png"/>
                        <div class="mui-media-body">游戏资讯</div>
                      </router-link>
                    </div>
                  </li>
                  <li class="mui-table-view-cell mui-media" style="background-color:#171A21">
                    <div class="mui-navigate-right">
                      <div @click="logout" class="mui-navigate-right">
                        <div class="mui-media-body">
                          <img class="mui-media-object mui-pull-left" src="../assets/images/24.png"/>
                          <p style="color:#007aff ">退出登录</p>
                        </div>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <!--未登录-->
              <div v-else>
                <div class="member">
                  <div class="header-con">
                    <router-link :to="{name:'login'}" class="mui-navigate-right">
                      <div class="user-info">
                        <div class="avatar-con">
                          <div class="avatar">
                            <img src="../assets/images/avatar_default.png" class="image-info">
                          </div>
                        </div>
                        <div class="person-con">
                          <span>登录/注册</span>
                        </div>
                      </div>
                    </router-link>
                  </div>
                </div>
              </div>

                <!-- 头像 -->
                <!--<a class="change"></a>-->
                <!-- 分类 -->
            </div>
        </transition>
    </div>
</template>
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script>
  import {mapState,mapGetters} from 'vuex'
    export default {
      name: "sideBar",

        components: {},

        data() {
            return {
              adatar:''
            }
        },
        methods: {

          //头像选择
          fileChange(e) {
            var that = this;
            // 保存files的信息
            var file = e.target.files[0];
            var reader = new FileReader();
            reader.onload = function(e){
              that.adatar  = e.target.result;
            }
            // 读取file对象的数据
            reader.readAsDataURL(file);
          },
          logout(){
            this.$http.get('logout');
            this.$store.commit('user/logout')
            this.$auth.setAuthorization('');
            this.$toast('退出成功')
          },
            hideSide: function () {
                this.$store.dispatch('hideSideBar');
            }
        },
        computed: {
          ...mapState({
            username:state=>state.user.username
          }),
          ...mapGetters(
            'user',{isLogin:'isLogin'}
          ),
            isRellyShow() {
                return this.$store.getters.isShowMethod;
            }
        },
    }
</script>

<style scoped>
    .menu-mask {
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        opacity: 1;
        z-index: 10;
        background: rgba(0, 0, 0, 0.5);
    }

    .side-content {
        z-index: 11;
        position: fixed;
        width: 286px;
        height: 100%;
      background: linear-gradient(90deg,#282A32,#233E40);
        top: 0;
        left: 0;
        bottom: 0;
        -webkit-overflow-scrolling: touch;
    }

    .change {
        display: block;
        width: 284px;
        height: 200px;
        background: url(http://p3.qhimg.com/t0134c65e59012a1257.png) no-repeat center;
        background-size: cover;
        border: 1px solid #fff;
        overflow: hidden;
    }

</style>

<style lang="scss" scoped>
  .mui-table-view .mui-media,
  .mui-table-view .mui-media-body {
    line-height: 42px;
  }
  .mui-table-view-cell:after {
    left: 0;
  }
  .member {
    margin-bottom: 15px;
    .header-con {
      padding: 10px;
      background: linear-gradient(90deg,#282A32,#233E40);;
      .user-info {
        position: relative;
        overflow: hidden;
        width: 100%;
        height: 120px;
        background: linear-gradient(-45deg, #eeaa84, #e74579, #6cabd5, #76d5ac);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        @keyframes gradientBG {
          0% {
            background-position: 0% 50%;
          }
          50% {
            background-position: 100% 50%;
          }
          100% {
            background-position: 0% 50%;
          }
        }
        box-shadow: 0 0.1rem 0.25rem #f8e3c6;
        .avatar-con {
          position: absolute;
          left: 15px;
          top: 50%;
          transform: translateY(-50%);
          .avatar {
            width: 60px;
            height: 60px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 15);
            border: 1px solid hsla(0, 0%, 100%, 0.4);
            border-radius: 50% 50%;
            .image-info {
              width: 100%;
              height: 100%;
            }
          }
        }
        .person-con {
          position: absolute;
          left: 90px;
          top: 50%;
          transform: translateY(-50%);
          color: #fff;
        }
      }
    }
  }
</style>

