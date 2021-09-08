<template>
  <div class="b" style="height: 100vh;width: 100%;">
  <div class="dowebok">
    <div class="form-item">
      <input v-model="regForm.username" type="text"  placeholder="请输入账号" />
    </div>
    <div class="form-item">
      <input v-model="regForm.password" type="password" placeholder="请输入密码" />

    </div>
    <div class="form-item">
      <input type="password" ref="pwdConfirm"  placeholder="请确认密码" />
    </div>
    <div class="form-item">
      <input v-model="regForm.email" type="email" placeholder="请输入邮箱" />
    </div>
    <div class="form-item">
      <button @click="register">注册</button>
      <div class="reg-bar">

      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      regForm: {
        username: '',
        password: '',
        email: ''
      }
    }
  },
  methods: {
    register: function () {
      var pwdConfirm = this.$refs.pwdConfirm.value
      if (this.regForm.username === '') {
        this.$toast('账号不能为空')
        return
      } else if (this.regForm.password === '') {
        this.$toast('密码不能为空')
        return
      } else if (this.regForm.password != pwdConfirm) {
        this.$toast('密码两次输入不一致')
        return
      } else if (this.regForm.email === '') {
        this.$toast('邮箱不能为空')
        return
      }
      this.$indicator.open({
        text: '注册中'
      })
      this.$http.post('register', this.regForm).then(res => {
        this.$indicator.close()
        if (res.data.code === 0) {
          this.$toast(res.data.msg)
        } else {
          this.$store.commit('user/setUser', res.data.data)
          this.$auth.setAuthorization(res.data.data.session_id)
          this.$toast(res.data.msg)
          // this.$router.replace({ name: 'user' })
          this.$router.go(-2)
        }
      }).catch(() => {
        this.$toast('注册失败')
      })
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
    }
  }

</style>

<!--<style lang="scss" scoped>-->
<!--.mui-input-group {-->
  <!--margin-top: 10px;-->
  <!--background-color: transparent;-->
<!--}-->
<!--.mui-input-group label {-->
  <!--width: 22%;-->
<!--}-->
<!--.mui-input-row:last-child {-->
  <!--background: #fff;-->
<!--}-->
<!--.mui-input-row {-->
  <!--margin-top: 20px;-->
  <!--background: #fff;-->
<!--}-->
<!--.mui-input-row label ~ input,-->
<!--.mui-input-row label ~ select,-->
<!--.mui-input-row label ~ textarea {-->
  <!--width: 78%;-->
<!--}-->
<!--.link-area {-->
  <!--display: block;-->
  <!--margin-top: 25px;-->
  <!--text-align: center;-->
<!--}-->
<!--.mui-content-padded {-->
  <!--margin-top: 30px;-->
<!--}-->
<!--</style>-->

