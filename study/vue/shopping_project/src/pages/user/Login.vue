<template>
    <!--<div class="login">-->
        <!--<div class="mui-content">-->
            <!--<form class="mui-input-group">-->
                <!--<div class="mui-input-row">-->
                    <!--<label>账号</label>-->
                    <!--<input v-model="loginForm.username" type="text" class="mui-input-clear mui-input" placeholder="请输入账号"/>-->
                <!--</div>-->
                <!--<div class="mui-input-row">-->
                  <!--<label>密码</label>-->
                    <!--<input v-model="loginForm.password" type="password" class="mui-input-clear mui-input" placeholder="请输入密码"/>-->
                <!--</div>-->
            <!--</form>-->
            <!--<div class="mui-content-padded">-->
                <!--<button class="mui-btn mui-btn-block mui-btn-primary" @click="login">登录</button>-->
                <!--<div class="link-area"><a @click="register">还没有账号？前往注册</a></div>-->
            <!--</div>-->
        <!--</div>-->
      <!--</div>-->
  <div class="b" style="height: 100vh;width: 100%;">
  <div class="dowebok">
    <div class="form-item">
      <input v-model="loginForm.username" type="text"  placeholder="请输入账号"/>
    </div>
    <div class="form-item">
      <input v-model="loginForm.password" type="password"  placeholder="请输入密码"/>
    </div>
    <div class="form-item">
      <button id="submit" @click="login">登 录</button></div>

    <div class="reg-bar">

      <a class="reg" href="javascript:" @click="register">立即注册</a>

      <!--<a class="forget" href="javascript:">忘记密码</a>-->

    </div>
  </div>
  </div>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                loginForm:{
                    username:'',
                    password:''
                }
            }
        },
        methods:{
            login(){
                if (this.loginForm.username===''||this.loginForm.password===''){
                    this.$toast('账号或者密码不能为空')
                } else {
                    this.$http.post('login',this.loginForm).then(res=>{
                        if (res.data.code===0){
                            this.$toast(res.data.msg)
                        } else {
                            this.$store.commit('user/setUser',res.data.data);
                            //将响应中的sessionid值保存到auth中
                            this.$auth.setAuthorization(res.data.data.session_id);
                            this.$toast(res.data.msg);
                            //跳转
                            this.$router.go(-1)
                        }
                    }).catch(err=>{
                        this.$toast('登录失败'+err)
                    })

                }
            },
            register(){
                //页面跳转
                this.$router.push({name:'register'})
            }
        }
    }
</script>



<style lang="scss" scoped>
  .form-item { position: relative; width: 360px; margin: 0 auto; padding-bottom: 30px;}

  .form-item input { width: 288px; height: 48px; padding-left: 70px; border: 1px solid #0f6674; border-radius: 25px; font-size: 18px; color: #0f6674; background-color: rgba(255,255,255,0); outline: none;}

  .form-item button { width: 360px; height: 50px; border: 0; border-radius: 25px; font-size: 18px; color: #1c7430; outline: none; cursor: pointer; background-color: white; }

  .reg-bar { width: 360px; margin: 20px auto 0; font-size: 14px; overflow: hidden;}

  .reg-bar a { color: #0f6674; text-decoration: none; }

  .reg-bar a:hover { text-decoration: underline; }

  .reg-bar .reg { float: left; }

  .dowebok ::-webkit-input-placeholder { font-size: 18px; line-height: 1.4; color: #fff;}

  .dowebok :-moz-placeholder { font-size: 18px; line-height: 1.4; color: #fff;}

  .dowebok ::-moz-placeholder { font-size: 18px; line-height: 1.4; color: #fff;}

  .dowebok :-ms-input-placeholder { font-size: 18px; line-height: 1.4; color: #fff;}

  @media screen and (max-width: 500px) {
    * { box-sizing: border-box; }

    .dowebok { position: relative; width: auto; height: auto; margin: 0 30px; border: 0; border-radius: 0; top: 50px}

    .form-item { width: auto; }

    .form-item input, .form-item button, .reg-bar { width: 100%; }

    .b{
      background: linear-gradient(45deg, Orange, #e74579, #6cabd5, #76d5ac);
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
    }
  }

</style>


