<template>
    <div>
      <div>
        <swiper :imgList="imgList"></swiper>
      </div>
        <div class="menu">
            <div class="menu-left">
                <ul>
                    <li class="menu-item" v-for="(menu,index) in menus" :key="index"
                        :class="{current:index===currentIndex}" @click="clickList(index)" ref="menuList">
                        <p class="text">{{menu.name}}</p>
                    </li>
                </ul>
            </div>
            <div class="menu-right" ref="itemList">
                <ul>
                    <li class="cate" v-for="(menu,index1) in menus" :key="index1">
                        <!--<h4 class="cate-title">{{menu.name}}</h4>-->
                        <ul class="cate-item">
                            <li v-for="(item,index2) in menu.sub" :key="index2">
                                <router-link class="cate-item-wrapper"
                                             :to="{name:'goods_list',params:{category_id:item.id}}">
                                  <div class="a">
                                    <div class="cate-item-img">
                                        <img :src="item.image">
                                    </div>
                                    <span>{{item.name}}</span>
                                  </div>
                                </router-link>
                            </li>
                        </ul>
                    </li>
                  <li class="cate-bottom"></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
  import Swiper from '../components/swiper'

    import BScroll from 'better-scroll'
    export default {
        name: "Category",

      components: {
        Swiper
      },

        data(){
            return{
              imgList:[],
                menus:[],
                //currentIndex:0,
                rightHeight:[],//右边菜单每一项的高度
                scrollY:0//记住右菜单的滚动距离
            }
        },

        created(){
          this.getImgList()

            this.$indicator.open({
                text:"加载中ing",

            });
            this.$http.get('category').then(res=>{
                this.menus=res.data.data;
                this.$indicator.close()
            })
        },
        methods:{

          getImgList(){
            //this.$indicator是MintUI中的组件
            this.$indicator.open({
              text:"加载中"
            })
            this.$http.get('imglist').then(res=>{
              this.$indicator.close()
              if(res.data.code==0)
              {
                this.$toast('加载轮播图失败')
              }
              else {
                this.imgList=res.data.data
              }
            })
          },

            clickList(index){
                //this.currentIndex=index;
                this.scrollY=this.rightHeight[index];
                //参数1：0，表示左右不动，参数2：Y
                this.RightBscroll.scrollTo(0,-this.rightHeight[index])
            },
            _initBScroll(){
                this.leftBscroll=new BScroll('.menu-left',{
                    click:true,
                    mouseWheel:true,
                    probeType:3//实时触发scroll事件
                });
                this.RightBscroll=new BScroll('.menu-right',{
                    click:true,
                    mouseWheel:true,
                    probeType:3
                });
                this.RightBscroll.on('scroll',(pos)=>{
                    this.scrollY=Math.abs(pos.y);
                })
            },
            _initRightHeight(){
                let itemArray=[];
                let top=0;
                itemArray.push(top);
                let allList=this.$refs.itemList.getElementsByClassName('cate');
                Array.prototype.slice.call(allList).forEach(li=>{
                    top+=li.clientHeight;
                    itemArray.push(top);
                });
                let bottom=this.$refs.itemList.getElementsByClassName('cate-bottom')[0]
              bottom.style.height=this.$refs.itemList.clientHeight/1.2+'px';
                this.rightHeight=itemArray
            },
          _initLeftScroll(index)
          {
            let menu=this.$refs.menuList
            let el=menu[index]
            //scrollTo:参数x，y，动画的时间和动画的效果
            //-100避免左边的菜单频繁的发生自动混动
            this.leftBscroll.scrollTo(el,300,0,-100);
          }
        },
        watch:{
            menus(){
                //$nextTick是vue中异步函数
                this.$nextTick(( )=>{
                    this._initBScroll();
                    this._initRightHeight();
                })
            }
        },
        computed:{
            currentIndex(){
                //当srcollY发生变化时，修改左边菜单项的激活项
                const {scrollY,rightHeight}=this;
                //从右边菜单查找元素，返回元素列表
                return rightHeight.findIndex((top,index)=>{
                  if(index===rightHeight.length-2){
                    return true;
                  }
                    if (scrollY >= top && scrollY < rightHeight[index + 1])
                    {
                        this._initLeftScroll(index)
                        return true;
                    }
                })
            }
        }
    }
</script>

<style lang="scss" scoped>
    ul {
        margin: 0;
        padding: 0;
    }
    li {
        list-style: none;
    }
    .menu {
        display: flex;
        position: absolute;
        text-align: center;
        top: 240px;
        bottom: 50px;
        width: 100%;
        overflow: hidden;
      .menu-left {
            flex: 0 0 80px;
            width: 80px;
        background: linear-gradient(180deg, #1E2630, #171A21);
            .menu-item {
                height: 60px;
                width: 100%;
                .text {
                    width: 100%;
                    line-height: 54px;
                    margin-bottom: 0;
                   color: white;
                }
            }
            .current {
                width: 100%;
                background: #040505;
                .text {
                    color: red;
                }
            }
        }
        .menu-right {
            flex: 1;
          background: linear-gradient(90deg,#282A32,#233E40);
            .cate {
                height: 100%;
                .cate-title {
                    margin: 0;
                    text-align: left;
                    font-size: 14px;
                    color: #333;
                    font-weight: bold;
                    padding: 10px;
                }
                .cate-item {
                    padding: 5px 4px 10px;
                    display: flex;
                    overflow: hidden;
                    flex-flow: row wrap;
                    li {
                        width: 50%;
                      height: 135px;
                        .cate-item-wrapper {
                            .cate-item-img {
                                width: 100%;
                                img {
                                    width: 100px;
                                    height: 100px;
                                }
                            }
                            span {
                                display: inline-block;
                                font-size: 14px;
                                color: white;
                            }
                        }
                    }
                }
            }
        }
    }
  .a{
    /*background: #ffffff;*/
    margin:10px 0px 0px 10px;
  }
</style>
