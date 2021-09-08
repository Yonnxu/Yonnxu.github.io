<template>
  <div class="b" style="height: 100vh;width: 100%;">
    <div class="dowebok">
      <div class="form-item">
        <input v-model="form.name" type="text" class="mui-input-clear" placeholder="请输入收件人姓名" />
      </div>
      <div class="form-item">
        <input v-model="form.tel" type="text" class="mui-input-clear" placeholder="请输入手机号" />
      </div>
      <div class="form-item">
  <input v-model="form.area" type="text" class="mui-input-clear" placeholder="所在地区" @click="choose" />
  <div class="divwrap">
    <div class="mask" @click="choose" v-show="show"></div>
    <v-distpicker v-show="show" type="mobile" @province="onChangeProvince" @city="onChangeCity" @area="onChangeArea"
                  :province="newInfo.province" :city="newInfo.city" :area="newInfo.district"></v-distpicker>
  </div>
      </div>
      <div class="form-item">
  <input v-model="form.detail" type="text" class="mui-input-clear" placeholder="请输入详细地址" />
      </div>
      <div class="form-item">
  <button @click="save" type="button" class="mui-btn mui-btn-primary mui-btn-block">确认</button>
  <button v-show="id" @click="del" type="button" class="mui-btn mui-btn-danger mui-btn-block">删除</button>
        <div class="reg-bar">

        </div>
      </div>
    </div>
  </div>


  <!--<form class="mui-input-group">-->
    <!--<div class="mui-input-row">-->
      <!--<label class="tit">收件人</label>-->
      <!--<input v-model="form.name" type="text" class="mui-input-clear" placeholder="请输入收件人姓名" />-->
    <!--</div>-->
    <!--<div class="mui-input-row">-->
      <!--<label class="tit">联系方式</label>-->
      <!--<input v-model="form.tel" type="text" class="mui-input-clear" placeholder="请输入手机号" />-->
    <!--</div>-->
    <!--<div class="mui-input-row">-->
      <!--<label class="tit">所在地区</label>-->
      <!--<input v-model="form.area" type="text" class="mui-input-clear" placeholder="所在地区" @click="choose" />-->
      <!--<div class="divwrap">-->
        <!--<div class="mask" @click="choose" v-show="show"></div>-->
        <!--<v-distpicker v-show="show" type="mobile" @province="onChangeProvince" @city="onChangeCity" @area="onChangeArea"-->
          <!--:province="newInfo.province" :city="newInfo.city" :area="newInfo.district"></v-distpicker>-->
      <!--</div>-->
    <!--</div>-->
    <!--<div class="mui-input-row">-->
      <!--<label class="tit">详细地址</label>-->
      <!--<input v-model="form.detail" type="text" class="mui-input-clear" placeholder="请输入详细地址" />-->
    <!--</div>-->
    <!--<div class="mui-button-row">-->
      <!--<button @click="save" type="button" class="mui-btn mui-btn-primary mui-btn-block">确认</button>-->
      <!--<button v-show="id" @click="del" type="button" class="mui-btn mui-btn-danger mui-btn-block">删除</button>-->
    <!--</div>-->
  <!--</form>-->
</template>

<script>
import VDistpicker from 'v-distpicker'

export default {
  data () {
    return {
      form: {
        name: '',
        tel: '',
        area: '',
        detail: ''
      },
      show: false,     // 是否显示遮罩层
      newInfo: {
        province: '', // 省
        city: '',     // 市
        area: '',     // 区
      }
    }
  },
  props: ['id'],
  created () {
    this.getAddress()
  },
  methods: {
    getAddress () {
      if (!this.id) {
        return
      }
      this.$indicator.open({
        text: '加载中'
      })
      var params = { id: this.id }
      this.$http.get('address/edit', { params: params }).then(res => {
        this.$indicator.close()
        window.console.log(res.data)
        if (res.data.code === 0) {
          this.$toast(res.data.msg)
        } else if (res.data.code === 1) {
          this.form = res.data.data
        } else if (res.data.code === 2) {
          this.$router.push({ name: 'login' })
        }
      })
    },
    choose () {
      this.show = !this.show
    },
    onChangeProvince (data) {
      this.newInfo.province = data.value
    },
    onChangeCity (data) {
      this.newInfo.city = data.value
    },
    onChangeArea (data) {
      this.newInfo.area = data.value
      this.form.area = this.newInfo.province + '-' + this.newInfo.city + '-' + this.newInfo.area
      this.show = false
    },
    save () {
      this.$indicator.open({
        text: '提交中'
      })
      this.form.id = this.id
      this.$http.post('address/save', this.form).then(res => {
        this.$indicator.close()
        if (res.data.code === 0) {
          this.$toast(res.data.msg)
        } else if (res.data.code === 1) {
          this.$toast(res.data.msg)
          this.$router.go(-1)
        } else if (res.data.code === 2) {
          this.$router.push({ name: 'login' })
        }
      })
    },
    del () {
      this.$indicator.open({
        text: '删除中'
      })
      this.form.id = this.id
      this.$http.post('address/del', this.form).then(res => {
        this.$indicator.close()
        if (res.data.code === 0) {
          this.$toast(res.data.msg)
        } else if (res.data.code === 1) {
          this.$toast(res.data.msg)
          this.$router.go(-1)
        } else if (res.data.code === 2) {
          this.$router.push({ name: 'login' })
        }
      })
    }
  },
  components: {
    'v-distpicker': VDistpicker
  }
}
</script>

<style lang="scss" scoped>
.mui-input-group .mui-button-row {
  height: auto;
}
.mui-input-clear {
  font-size: 14px;
}
.mui-input-group:before {
  list-style: none;
}
.mui-button-row {
  margin-top: 20px;
  button {
    margin: 20px 0;
    padding: 10px 0;
  }
}
.tit {
  color: white;
}
input::-webkit-input-placeholder {
  color: #999;
}
input::-moz-placeholder {
  /* Mozilla Firefox 19+ */
  color: #999;
}
input:-moz-placeholder {
  /* Mozilla Firefox 4 to 18 */
  color: #999;
}
input:-ms-input-placeholder {
  /* Internet Explorer 10-11 */
  color: #999;
}
.divwrap > .mask {
  background: #000;
  opacity: 0.3;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
.divwrap > .distpicker-address-wrapper {
  color: #999;
  background: #fff;
  border-top: 1px solid #ccc;
  z-index: 1;
  height: 300px;
  overflow-y: auto;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
}




.form-item { position: relative; width: 360px; margin: 0 auto; padding-bottom: 30px;}

.form-item input { width: 288px; height: 48px; padding-left: 70px; border: 1px solid #0f6674; border-radius: 25px; font-size: 18px; color: white; background-color: rgba(255,255,255,0); outline: none;}

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



