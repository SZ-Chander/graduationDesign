<!--
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 09:56:52
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-11 01:20:42
-->
<template>
  <div class="all">
    <!-- 登录框 -->
    <div class="login">
      <!-- 左边
      <div class="left">111</div> -->
      <!-- 右边 -->
      <div class="right">
        <h1>登录</h1>
        <div>
          <el-form ref="formRef" :model="form" :rules="rules">
            <!-- 账号 -->
            <el-form-item label="账号" prop="id">
              <el-input v-model="form.id" placeholder="请输入账号" />
            </el-form-item>
            <!-- 密码 -->
            <el-form-item label="密码" prop="password">
              <el-input v-model="form.password" placeholder="请输入密码" />
            </el-form-item>
          </el-form>
          <div class="button">
            <el-button @click="login">登录</el-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ElMessage } from 'element-plus'
import { logins } from '@/api/login'


// 创建路由
const router = useRouter()
// 创建vuex实例
const store = useStore()

// 表单数据
const formRef = ref(null)
const form = ref({
	privacy: 0
})
// 表单限制条件
const rules = ({
  id:[
    {
      require:true,
      message:'请输入账号',
      trigger:'blur'
    }
  ],
  password:[
    {
      require:true,
      message:'请输入密码',
      trigger:'blur'
    }
  ]
})

// 登录信息
const main = ref(null)

// 登录按钮
const login =() => {
  formRef.value.validate((valid) => {
		if (valid) {
      // 调用登录接口
      logins(form.value.id,form.value.password)
        .then((res) => {
          main.value = res
          // 将身份验证信息存到store里面去
          // store.state.token = res.data.list[0].authToken
          console.log(store.state.token)
          // 判断数据是否返回，返回则跳转
          if(true){
            router.push({
              path:`/Main`
            })
          }
        })
      
		}
    console.log(main.value)
	})
}

</script>
<script>
export default {
  name:'Home'
}
</script>

<style lang="scss" scoped>
.all {
  background-image: linear-gradient(120deg, #3498db, #8e44ad);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 45.5rem;

  .login {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
    width: 384px;

    display: flex;
    justify-content: space-around;

    h1 {
      display: flex;
      justify-content: center;
    }
  }
}
</style>